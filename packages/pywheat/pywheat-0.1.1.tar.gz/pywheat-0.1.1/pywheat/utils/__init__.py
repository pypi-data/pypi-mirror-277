# coding=utf-8

#******************************************************************************
#
# Utils
# 
# version: 1.1
# Copyright: (c) October 2023
# Authors: Ernesto Giron (e.giron.e@gmail.com)
#
#
# This source is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# This code is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# A copy of the GNU General Public License is available on the World Wide Web
# at <http://www.gnu.org/copyleft/gpl.html>. You can also obtain it by writing
# to the Free Software Foundation, Inc., 59 Temple Place - Suite 330, Boston,
# MA 02111-1307, USA.
#
#******************************************************************************

from __future__ import absolute_import, division, print_function

import warnings
warnings.simplefilter('ignore')
warnings.filterwarnings('ignore')

import os, sys, gc
import pathlib
import datetime as dt
import numpy as np
import pandas as pd
from tqdm import tqdm
import matplotlib
from matplotlib import pyplot as plt
#import matplotlib.gridspec as gridspec
#from matplotlib.collections import PathCollection
import matplotlib.dates as mdates
from matplotlib.patches import Rectangle
import seaborn as sns
from joblib import Parallel, delayed
from pathlib import Path
from typing import Callable, Iterable, TypeVar

import subprocess
import pyarrow as pa
import pyarrow.parquet as pq
#import pyarrow.compute as pc

#from ..pheno import estimate_emergence_by_bruteforce, estimate_heading_by_bruteforce
#from ..pheno import estimate_anthesis_by_bruteforce, estimate_maturity_by_bruteforce
#from ..pheno import determine_phenology_stages
from .metrics import getScores, getTraitScores


'''
    Usage: Weather["date"] = Weather.apply(zfilldate, axis=1)

'''
def zfilldate(df):
    y = str(df['Year'])
    m = str(df["Month"])
    d = str(df["Day"])
    ymd =  y + m.zfill(2) + d.zfill(2)
    ymd = dt.datetime.strptime(ymd, "%Y%m%d")
    return ymd #.strftime('%Y-%m-%d')

def toInt(value):
    try:
        return int(value)
    except Exception: #(ValueError, TypeError):
        return np.nan    # leave unchanged
    
def getPhenologyDateAfterSowing(sowingdate, daysaftersowing):
    try:
        #return sowingdate + pd.DateOffset(days=int(daysaftersowing))
        return (sowingdate + pd.DateOffset(days=int(daysaftersowing))).strftime('%Y-%m-%d')
    except Exception: #(ValueError, TypeError):
        return np.nan

def getDOY(value):
    try:
        doy = int(value.strftime('%j'))
        return doy
    except Exception: #(ValueError, TypeError):
        return np.nan    # leave unchanged
    
def getDAP(stagedate, sowing):
    try:
        return int((stagedate - sowing).days) #.dt.days
    except Exception: #(ValueError, TypeError):
        return np.nan    # leave unchanged

# Get Datetime for DATE columns
def getFullDate(YrDOY):
    dtime = dt.datetime.strptime(YrDOY, '%y%j')
    return dtime

# Read weather file .WTH
def readWeatherStationData(input_file=None):
    '''Read DSSAT weather file for the experimental station'''
    if (input_file is None):
        #input_file = os.path.join(DSSAT_PATH, 'Weather', "{}.WTH".format(params['filex']))
        print("Path of the weather .WTH file not found.")
        return
    if (os.path.exists(input_file)):
        header = []
        rows = []
        with open(input_file, 'r', encoding='cp1252' ) as f:
            file_pos = 0
            while True:
                line = f.readline()
                if not line:
                    break
                if ( (len(line.strip())!=0) and (line[0]!= '!') and (line[0]!='*')):
                    if ( line.startswith('@DATE')):
                        header = line.replace('@','').strip().split(' ')
                        header = [x for x in header if x!='']
                    else:
                        values = line.strip().split(' ')
                        values = [x for x in values if x!='']
                        if (len(values)==len(header)):
                            rows.append(values)
        #print(header)
        df = pd.DataFrame(data=rows, columns=header)
        # Get forward data from sowing date 
        df['DATETIME'] = pd.to_datetime(df['DATE'].apply(lambda x: getFullDate(x)), format='%Y-%m-%d' )
        #df = df[df['DATETIME']>=params['plantingDates'][0]]
        # rename columns for pywheat
        df.rename(columns={'DATE':'YYDOY','DATETIME':'DATE'}, inplace=True)
        return df
    else:
        print("Weather file not found")
        

# Read cultivars file WHAPS0XX.CUL for NWheat model
def readCultivarConfig(input_file=None):
    '''Read DSSAT configuration cultivar file for NWheat model'''
    if (input_file is None):
        #input_file = os.path.join(DSSAT_PATH, 'Genotype', 'WHAPS047.CUL')
        print("Path of the cultivar file not found.")
        return
    if (os.path.exists(input_file)):
        header = []
        rows = []
        with open(input_file, 'r', encoding='cp1252' ) as f:
            file_pos = 0
            while True:
                line = f.readline()
                if not line:
                    break
                if ( (len(line.strip())!=0) and (line[0]!= '!') and (line[0]!='*')):
                    if ( line.startswith('@VAR#')):
                        header = line.replace('@','').replace('#','').replace('VRNAME..........','VRNAME').strip().split(' ')
                        header = [x for x in header if x!='']
                    else:
                        values = line.strip().split(' ')
                        # check out the VRNAME column with name using blank spaces
                        VRNAME = line[7:25].strip()
                        if (len(VRNAME.split(' '))>1):
                            # replace space with underscore
                            VRNAME = VRNAME.replace(' ','_') #.strip()
                            values = (line[0:7] + ' ' + VRNAME + line[25:-1]).strip().split(' ')
                        values = [x for x in values if x!='']
                        if (len(values)==len(header)):
                            rows.append(values)
        #print(header)
        return pd.DataFrame(data=rows, columns=header)
    else:
        print("Cultivar file not found")


# Read ecotypes file WHAPS0XX.ECO for NWheat model
def readEcotypesConfig(input_file=None):
    '''Read DSSAT configuration ecotypes file for NWheat model'''
    if (input_file is None):
        #input_file = os.path.join(DSSAT_PATH, 'Genotype', 'WHAPS047.eco')
        #if (not os.path.exists(input_file)):
        #    input_file = os.path.join(DSSAT_PATH, 'Genotype', 'WHAPS047.ECO')
        print("Path of the ecotypes file not found.")
        return
    if (os.path.exists(input_file)):
        header = []
        rows = []
        with open(input_file, 'r', encoding='cp1252' ) as f:
            file_pos = 0
            while True:
                line = f.readline()
                if not line:
                    break
                if ( (len(line.strip())!=0) and (line[0]!= '!') and (line[0]!='*')):
                    if ( line.startswith('@ECO#')):
                        header = line.replace('@','').replace('#','').replace('ECONAME.........','ECONAME').strip().split(' ')
                        header = [x for x in header if x!='']
                    else:
                        values = line.strip().split(' ')
                        # check out the ECONAME column with name using blank spaces
                        ECONAME = line[7:25].strip()
                        if (len(ECONAME.split(' '))>1):
                            # replace space with underscore
                            ECONAME = ECONAME.replace(' ','_')
                            values = (line[0:7] + ' ' + ECONAME + line[25:-1]).strip().split(' ')
                        values = [x for x in values if x!='']
                        if (len(values)<len(header)):
                            values.append('') #TSEN
                            values.append('') #CDAY
                        if (len(values)==len(header)):
                            rows.append(values)
        #print(header)
        return pd.DataFrame(data=rows, columns=header)
    else:
        print("Ecotype file not found")
        
#
def readPlantGro(input_file=None, RUN_START=1, RUN_END=2):
    '''Read first run simulation from PlantGro.OUT file
    '''
    if (input_file is None):
        print("Path of the PlantGro.OUT file not found.")
        return
    if (os.path.exists(input_file)):
        StartLine = 0
        EndLine = 1
        cols = []
        rows = []
        with open(input_file, 'r', encoding='cp1252', buffering=100000 ) as f: 
            file_pos = 0
            while True:
                line = f.readline()
                if not line:
                    break
                ls = line.split(':')[0].strip()
                if (ls=='*RUN{:>4}'.format(RUN_START)):
                    StartLine = f.tell() #returns the location of the next line
                elif (ls=='*RUN{:>4}'.format(RUN_END)):
                    EndLine = f.tell() 
            # Display lines
            file_pos = f.seek(StartLine)
            l2conv = False
            while file_pos != EndLine:
                line = f.readline()
                if not line:
                    break
                ls = line.split(':')[0].strip()
                if (line.startswith('@YEAR')):
                    pos_tmp = f.tell() 
                    cols = line.replace('@','').strip().split(' ')
                    cols = [x for x in cols if x!='']
                    l2conv = True
                elif (l2conv is True or line.startswith('*DSSAT')): #line.strip()!=' '):
                    values = line.strip().split(' ')
                    values = [x for x in values if x!='']
                    if (len(values)==len(cols)):
                        rows.append(values)
                else:
                    l2conv = False

                file_pos += len(line)
                
        return pd.DataFrame(data=rows, columns=cols)
    else:
        print("PlantGro.OUT file not found!")
#

def createWHA(df, output_file=None):
    if (output_file is None):
        print("Input file not valid")
        return False
    hoy = dt.date.today().strftime('%Y-%m-%d')
    with open(output_file, 'w', encoding='cp1252', newline='\r\n' ) as f:
        headerWHA = f"""*EXP. DATA (A): CIMMYT IWIN Project 2022 - 2024                 

! File last edited on day {hoy} by egiron.
! 
"""
        f.writelines(headerWHA)
        f.writelines("@TRNO   HWAM  ADAT  MDAT\n")
        for idx in df.index:
            TRNO = idx + 1
            HWAM = int(df.iloc[idx]['ObsYield'] * 1000) if str(df.iloc[idx]['ObsYield'])!='nan' else -99
            ADAT = int(df.iloc[idx]['ObsAnthesisDAP']) if str(df.iloc[idx]['ObsAnthesisDAP'])!='nan' else -99
            MDAT = int(df.iloc[idx]['ObsMaturityDAP']) if str(df.iloc[idx]['ObsMaturityDAP'])!='nan' else -99
            f.writelines("{:>6}{:>6}{:>6}{:>6}\n".format(TRNO, HWAM, ADAT, MDAT ))
   


# ---------------------------
# Parquet file utils
# ---------------------------
"""coalesce_parquets.py
    gist of how to coalesce small row groups into larger row groups.
    Solves the problem described in https://issues.apache.org/jira/browse/PARQUET-1115
"""
def stream_to_parquet(path: Path, tables: Iterable[pa.Table]) -> None:
    try:
        first = next(tables)
    except StopIteration:
        return
    schema = first.schema
    with pq.ParquetWriter(path, schema) as writer:
        writer.write_table(first)
        for table in tables:
            table = table.cast(schema)  # enforce schema
            writer.write_table(table)


def stream_from_parquet(path: Path) -> Iterable[pa.Table]:
    reader = pq.ParquetFile(path)
    for batch in reader.iter_batches():
        yield pa.Table.from_batches([batch])


def stream_from_parquets(paths: Iterable[Path]) -> Iterable[pa.Table]:
    for path in paths:
        yield from stream_from_parquet(path)


"""Coalesce items into chunks. Tries to maximize chunk size and not exceed max_size.
    If an item is larger than max_size, we will always exceed max_size, so make a
    best effort and place it in its own chunk.
    You can supply a custom sizer function to determine the size of an item.
    Default is len.
    >>> list(coalesce([1, 2, 11, 4, 4, 1, 2], 10, lambda x: x))
    [[1, 2], [11], [4, 4, 1], [2]]
"""
T = TypeVar("T")
def coalesce( items: Iterable[T], max_size: int, sizer: Callable[[T], int] = len ) -> Iterable[list[T]]:
    batch = []
    current_size = 0
    for item in items:
        this_size = sizer(item)
        if current_size + this_size > max_size:
            yield batch
            batch = []
            current_size = 0
        batch.append(item)
        current_size += this_size
    if batch:
        yield batch


def coalesce_parquets(paths: Iterable[Path], outpath: Path, max_size: int = 2**20) -> None:
    tables = stream_from_parquets(paths)
    # Instead of coalescing using number of rows as your metric, you could
    # use pa.Table.nbytes or something.
    # table_groups = coalesce(tables, max_size, sizer=lambda t: t.nbytes)
    table_groups = coalesce(tables, max_size)
    coalesced_tables = (pa.concat_tables(group) for group in table_groups)
    stream_to_parquet(outpath, coalesced_tables)

def mergeParquetFiles(in_path, out_path, fname='merge', removeParts=False):
    paths = Path(in_path).glob("*.parquet")
    #print(list(paths))
    if not os.path.isdir(out_path):
        os.makedirs(out_path, exist_ok=True)
    
    coalesce_parquets(paths, outpath=os.path.join(out_path, "{}.parquet".format(fname)))
    print(pq.ParquetFile(os.path.join(out_path, "{}.parquet".format(fname) )).metadata)
    if (removeParts is True):
        try:
            shutil.rmtree(in_path)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

# ------------------------------



# --------------------------------------------------
# Draw Phenology
# --------------------------------------------------
def drawPhenology(gs=None, title='Phenological growth phases of Wheat', dpi=150,
                  dispPlants=True, topDAPLabel=True, timeSpanLabel=True, topNameStageLabel=True,
                  topNameStageLabelOpt=True, copyrightLabel=True, saveFig=True, showFig=True, 
                  path_to_save_results='./', fname='Phenological_Phases_Wheat', fmt='jpg'):
    
    if ('2.5' in gs):
        del gs['2.5'] # remove anthesis row
    df = pd.DataFrame(gs).T
    # Setup parameters for x-axes
    labels = ','.join([str(x) for x in df['istage_old']]).split(',')
    dap_values = ','.join([str(x) for x in df['DAP']]).split(',')
    tt_values = ','.join([str(x) for x in df['SUMDTT']]).split(',')
    date_values = ','.join([str(x) for x in df['date']]).split(',')
    doy_values = ','.join([str(x) for x in df['DOY']]).split(',')
    cropage_values = ','.join([str(x) for x in df['AGE']]).split(',')
    # Convert date strings (e.g. 2014-10-18) to datetime
    dates = list(df['date'])
    dates = [dt.datetime.strptime(d, "%Y-%m-%d") for d in dates]
    dates_Month_Year = [d.strftime('%b-%Y') for d in dates]
    dates_MMM_DD_YYYY = [d.strftime('%b %d, %Y') for d in dates]

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 5), dpi=dpi, constrained_layout=True)

    # -------------------------
    # Figure 1
    # -------------------------
    ax.scatter(dap_values, tt_values, c="#fff") # Don't show the points
    ax.set_title(f'{title}', fontsize=18, y=1.1, pad=16)
    #plt.xticks(rotation=90, fontsize=9)
    ax.xaxis.set_ticks([])
    ax.yaxis.set_ticks([])
    ax.grid(visible=False)
    ax.spines['top'].set_linestyle("dashed")
    ax.spines['top'].set_capstyle("butt")
    ax.spines['top'].set_linewidth(.2)  
    ax.spines['bottom'].set_color('black')
    ax.spines[['left',  'right']].set_visible(False)
    # format x-axis with 4-month intervals
    #ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    #ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    #plt.setp(ax.get_xticklabels(), rotation=0, ha="center")

    # ---------------------------
    # ---- Stages x-axis
    def dispXAxes_Phenology(v='Stage', xticklabels=[], centerLabel=False, c='green', ypos_axis=-0.05, 
                            xpos_tile=-0.1, ypos_title=-0.11,  fsize_title=12, fsize_labels=10):
        ax1 = ax.twiny()
        ax1.xaxis.set_ticks_position("bottom")
        ax1.xaxis.set_label_position("bottom")
        ax1.spines["bottom"].set_position(("axes", ypos_axis))
        ax1.spines['bottom'].set_color(c)
        ax1.spines[['left', 'top', 'right']].set_visible(False)
        ax1.set_xticks(np.array(range(0,9)))
        ax1.set_xticklabels(xticklabels, fontsize=fsize_labels)
        ax1.xaxis.label.set_color(c)
        ax1.tick_params(axis='x', colors=c)
        ax1.grid(visible=False)
        if (centerLabel):
            ax1.set_xlabel(f"{v}")
        else:
            ax1.text(xpos_tile, ypos_title, v, transform=ax.transAxes, fontsize=fsize_title, 
                     fontname='Monospace', color=c)

    # Display Stage or Phase name axis
    dispXAxes_Phenology(v='Stage', xticklabels=labels, centerLabel=False, c='green', ypos_axis=-0.05, 
                            xpos_tile=-0.1, ypos_title=-0.11, fsize_title=12, fsize_labels=10)
    # Display Phenology Date axis
    dispXAxes_Phenology(v='Date', xticklabels=dates_MMM_DD_YYYY, centerLabel=False, c='black', ypos_axis=-0.20, 
                            xpos_tile=-0.1, ypos_title=-0.27, fsize_title=12, fsize_labels=8)
    # Display Day of Year axis
    dispXAxes_Phenology(v='DOY', xticklabels=[f"{x}" for x in doy_values], centerLabel=False, 
                        c='purple', ypos_axis=-0.35, xpos_tile=-0.1, ypos_title=-0.43, fsize_title=12, fsize_labels=8)
    # Display Thermal time axis
    dispXAxes_Phenology(v='GDD', xticklabels=[f"{x} °C d" for x in tt_values], centerLabel=False, 
                        c='red', ypos_axis=-0.50, xpos_tile=-0.1, ypos_title=-0.57, fsize_title=12, fsize_labels=8)
    # ---------------------------

    ''' Display the icon of the plant over the figure '''
    def drawPlants(nstage=0, xpos=0.08, ypos=0.398, w=0.04, h=0.04):
        #print(pathlib.Path(__file__).parent.resolve())
        #icons_path = os.path.dirname(os.path.abspath(__file__)) # py2.7 & py3.x
        #icons_path = os.getcwd() +'/pywheat/data/whstages/stage_7.png'
        icons_path = os.path.join(pathlib.Path(__file__).parent.resolve(), '../data/whstages/',f"stage_{nstage}.png")
        img_stage = plt.imread(icons_path)
        newax = fig.add_axes([xpos, ypos, w, h], anchor='C', zorder=1)
        newax.imshow(img_stage)
        newax.axis('off')

    if (dispPlants):
        # ------ Stage 7
        drawPlants(nstage=7, xpos=0.08, ypos=0.398-0.005, w=0.04, h=0.04)
        # ------ Stage 8
        drawPlants(nstage=8, xpos=0.08+0.10, ypos=0.398-0.004, w=0.04, h=0.04)
        # ------ Stage 9
        drawPlants(nstage=9, xpos=0.08+0.195, ypos=0.398-0.002, w=0.055, h=0.055)
        # ------ Stage 1
        drawPlants(nstage=1, xpos=0.08+0.255, ypos=0.398+0.001, w=0.15, h=0.15)
        # ------ Stage 2
        drawPlants(nstage=2, xpos=0.08+0.325, ypos=0.398, w=0.22, h=0.22)
        # ------ Stage 3
        drawPlants(nstage=3, xpos=0.08+0.395, ypos=0.398, w=0.28, h=0.28)
        # ------ Stage 4
        drawPlants(nstage=4, xpos=0.08+0.485, ypos=0.398, w=0.32, h=0.32)
        # ------ Stage 5
        drawPlants(nstage=5, xpos=0.08+0.575, ypos=0.398, w=0.35, h=0.35)
        # ------ Stage 6
        drawPlants(nstage=6, xpos=0.08+0.805, ypos=0.398, w=0.08, h=0.08)
        # ---------------------------
        # Top Label of plants
        if (topDAPLabel):
            topLabel_DAP = [f"{x} days" for x in dap_values]
            fs=8
            clr = '#444'
            ax.text(-0.015, 0.1, topLabel_DAP[0], transform=ax.transAxes, fontsize=fs, color=clr)
            ax.text(0.1, 0.1, topLabel_DAP[1], transform=ax.transAxes, fontsize=fs, color=clr)
            ax.text(0.23, 0.15, topLabel_DAP[2], transform=ax.transAxes, fontsize=fs, color=clr)
            ax.text(0.34, 0.37, topLabel_DAP[3], transform=ax.transAxes, fontsize=fs, color=clr)
            ax.text(0.47, 0.56, topLabel_DAP[4], transform=ax.transAxes, fontsize=fs, color=clr)
            ax.text(0.59, 0.66, topLabel_DAP[5], transform=ax.transAxes, fontsize=fs, color=clr)
            ax.text(0.72, 0.74, topLabel_DAP[6], transform=ax.transAxes, fontsize=fs, color=clr)
            ax.text(0.90, 0.74, topLabel_DAP[7], transform=ax.transAxes, fontsize=fs, color=clr)
            ax.text(0.96, 0.16, topLabel_DAP[8], transform=ax.transAxes, fontsize=fs, color=clr)
    # ---------------------------
    if (timeSpanLabel):
        betweenLabel_AGE = [f"{x} d" for x in cropage_values]
        fs=7
        clr = 'darkgray'
        xpos_age = 0.05
        ypos_age = 0.015
        ax.text(xpos_age, ypos_age, betweenLabel_AGE[1], transform=ax.transAxes, fontsize=fs, color=clr)
        ax.text(xpos_age + 0.12, ypos_age, betweenLabel_AGE[2], transform=ax.transAxes, fontsize=fs, color=clr)
        ax.text(xpos_age + 0.245, ypos_age, betweenLabel_AGE[3], transform=ax.transAxes, fontsize=fs, color=clr)
        ax.text(xpos_age + 0.375, ypos_age, betweenLabel_AGE[4], transform=ax.transAxes, fontsize=fs, color=clr)
        ax.text(xpos_age + 0.50, ypos_age, betweenLabel_AGE[5], transform=ax.transAxes, fontsize=fs, color=clr)
        ax.text(xpos_age + 0.62, ypos_age, betweenLabel_AGE[6], transform=ax.transAxes, fontsize=fs, color=clr)
        ax.text(xpos_age + 0.75, ypos_age, betweenLabel_AGE[7], transform=ax.transAxes, fontsize=fs, color=clr)
        ax.text(xpos_age + 0.88, ypos_age, betweenLabel_AGE[8], transform=ax.transAxes, fontsize=fs, color=clr)

    if (topNameStageLabel):
        fs=10
        clr = 'green'
        ypos_phases = 0.94 #1.04
        ax.text(0.25, ypos_phases, 'Vegetative phase', ha='center', transform=ax.transAxes, fontsize=fs, color=clr, alpha=1)
        ax.text(0.60, ypos_phases, 'Reproductive phase', ha='center', transform=ax.transAxes, fontsize=fs, 
                color=clr, alpha=1)
        ax.text(0.84, ypos_phases, 'Grain Filling phase', ha='center', transform=ax.transAxes, fontsize=fs, 
                color=clr, alpha=1)
        # rectangles
        xy, w, h = (0, 0.92), 1, 1
        r = Rectangle(xy, w, h, fc='#f6fef6', ec='gray', lw=0.2, transform=ax.transAxes, zorder=2)
        ax.add_artist(r)

    if (topNameStageLabelOpt):
        fs=10
        clr = 'brown'
        ypos=0.85
        ax.text(0.47, ypos, 'Heading', transform=ax.transAxes, fontsize=fs, color=clr, alpha=0.5)
        ax.text(0.56, ypos, 'Anthesis', transform=ax.transAxes, fontsize=fs, color=clr, alpha=0.5)
        ax.text(0.84, ypos, 'Maturity', transform=ax.transAxes, fontsize=fs, color=clr, alpha=0.5)

    # Add vertical lines
    #vertLines = False
    #if (vertLines):
    #    clr='lightgray'
    #    #ax.axvline(0, ls='--', c=clr, linewidth=0.4, label="Vegetative phase", zorder=-1)
    #    #ax.axvline(2, ls='--', c=clr, linewidth=0.4, zorder=0)
    #    ax.axvline(4, ls='--', c=clr, linewidth=0.4, zorder=-1)
    #    ax.axvline(6, ls='--', c=clr, linewidth=0.4, zorder=-1)

    if (copyrightLabel):
        yr = dt.datetime.now().year
        ax.text(0.88, -0.75, f'Created with PyWheat © {yr}', transform=ax.transAxes, fontsize=7, 
                color='lightgray', zorder=2)

    # ---------------------------
    fig.tight_layout()
    fig.subplots_adjust(bottom=0.4) #hspace=0.5, wspace=0.5
    # Save in PDF
    hoy = dt.datetime.now().strftime('%Y%m%d')
    figures_path = path_to_save_results #os.path.join(path_to_save_results, '{}_{}'.format(dirname, hoy))
    if not os.path.isdir(figures_path):
        os.makedirs(figures_path)
    if (saveFig is True and fmt=='pdf'):
        fig.savefig(os.path.join(figures_path,"{}_{}.{}".format(fname, hoy, fmt)), 
                    bbox_inches='tight', orientation='portrait',  
                    edgecolor='none', transparent=False, pad_inches=0.5, dpi=dpi)

    if (saveFig==True and (fmt=='jpg' or fmt=='png')):
        fig.savefig(os.path.join(figures_path,"{}_{}.{}".format(fname, hoy, fmt)), 
                    bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none', transparent=False, dpi=dpi)
    
    if (showFig is True):
        fig.show()
    else:
        del fig
        plt.close();

# ---------------------------------------------
def display_GDD(df, growstages):
    df = df.copy()
    fig, ax1 = plt.subplots(1,1, figsize=(10,6))
    fig.subplots_adjust(top=0.9)
    sns.set_theme(style="whitegrid")
    ax1.scatter(x=df["DAP"].to_numpy(), y=df["AGE"].to_numpy(), label='GDD (Wheat)', color='#fff' )
    #g1 = sns.scatterplot(x="DAP", y="SUMDTT", data=df, label='GDD (Wheat)', 
    #                markers=False, color='red', ax=ax1)
    # 
    # Lines growing dates
    #7 - Fallow - 1997-12-17
    stage_7 = df.iloc[0]['DAP'] #int(df['DAP'][df['date']==growstages['7']['date']])
    #8 - Sowing - 1997-12-19
    stage_8 = df.iloc[1]['DAP'] #int(df['DAP'][df['date']==growstages['8']['date']])
    #9 - Germinate - 1998-01-01
    stage_9 = df.iloc[2]['DAP'] #int(df['DAP'][df['date']==growstages['9']['date']])
    #1 - Emergence - 1998-04-06
    stage_1 = df.iloc[3]['DAP'] #int(df['DAP'][df['date']==growstages['1']['date']])
    #2 - End Juveni - 1998-04-29
    stage_2 = df.iloc[4]['DAP'] #int(df['DAP'][df['date']==growstages['2']['date']])
    #3 - End Veg - 1998-05-14
    stage_3 = df.iloc[5]['DAP'] #int(df['DAP'][df['date']==growstages['3']['date']])
    #4 - End Ear Gr - 1998-05-23
    stage_4 = df.iloc[6]['DAP'] #int(df['DAP'][df['date']==growstages['4']['date']])
    #5 - Beg Gr Fil - 1998-06-18
    stage_5 = df.iloc[7]['DAP'] #int(df['DAP'][df['date']==growstages['5']['date']])
    #6 - Maturity - 
    stage_6 = df.iloc[8]['DAP'] #int(df['DAP'][df['date']==growstages['6']['date']])
    sp = 5
    vp = 1.0
    ax1.axvline(stage_7, ls='--', c='green', linewidth=0.8) #label="Fallow", 
    #ax1.text(0, .2, 'label', fontweight="bold", color='green', ha="left", va="center")
    an7 = ax1.annotate("{} - {}".format(growstages['7']['istage_old'], growstages['7']['date']), (stage_7-sp, vp), c='grey', fontsize=10)
    plt.setp(an7, rotation=90)
    ax1.axvline(stage_8, ls='--', c='green', linewidth=0.8) #label="Sowing", 
    an8 = ax1.annotate("{} - {}".format(growstages['8']['istage_old'], growstages['8']['date']), (stage_8, vp), c='grey', fontsize=10)
    plt.setp(an8, rotation=90)
    ax1.axvline(stage_9, ls='--', c='green', linewidth=0.8) #label="Germinate", 
    an9 = ax1.annotate("{} - {}".format(growstages['9']['istage_old'], growstages['9']['date']), (stage_9+2, vp), c='grey', fontsize=10)
    plt.setp(an9, rotation=90)
    ax1.axvline(stage_1, ls='--', c='green', linewidth=0.8) #label="Emergence", 
    an1 = ax1.annotate("{} - {}".format(growstages['1']['istage_old'], growstages['1']['date']), (stage_1-sp, vp), c='grey', fontsize=10)
    plt.setp(an1, rotation=90)
    ax1.axvline(stage_2, ls='--', c='green', linewidth=0.8) #label="End Juveni",
    an2 = ax1.annotate("{} - {}".format(growstages['2']['istage_old'], growstages['2']['date']), (stage_2-sp, vp), c='grey', fontsize=10)
    plt.setp(an2, rotation=90)
    ax1.axvline(stage_3, ls='--', c='green', linewidth=0.8) #label="End Veg", 
    an3 = ax1.annotate("{} - {}".format(growstages['3']['istage_old'], growstages['3']['date']), (stage_3-sp, vp), c='grey', fontsize=10)
    plt.setp(an3, rotation=90)
    ax1.axvline(stage_4, ls='--', c='green', linewidth=0.8) #label="End Ear Gr", 
    an4 = ax1.annotate("{} - {}".format(growstages['4']['istage_old'], growstages['4']['date']), (stage_4-sp, vp), c='grey', fontsize=10)
    plt.setp(an4, rotation=90)
    ax1.axvline(stage_5, ls='--', c='green', linewidth=0.8) #label="Beg Gr Fil", 
    an5 = ax1.annotate("{} - {}".format(growstages['5']['istage_old'], growstages['5']['date']), (stage_5-sp, vp), c='grey', fontsize=10)
    plt.setp(an5, rotation=90)
    ax1.axvline(stage_6, ls='--', c='green', linewidth=0.8) #label="Maturity", 
    an6 = ax1.annotate("{} - {}".format(growstages['6']['istage_old'], growstages['6']['date']), (stage_6-sp, vp), c='grey', fontsize=10)
    plt.setp(an6, rotation=90)

    plt.xticks(rotation=90)
    ax1.grid(visible=True, which='major', color='#d3d3d3', linewidth=0.25)
    #ax1.set_title('NWheat', fontsize=13)
    ax1.set_xlabel('Day after planting (DAP)', fontsize=14)
    #ax1.set_ylabel('Crop age (days)', fontsize=14)
    ax1.set_ylabel('')
    #ax1.legend(loc="best", fontsize=10)
    #ax1.get_legend().remove()
    #ax1.set_xticks([f'{str(x)}' for x in list(df['DAP'])])
    ax1.set_xticks(np.arange(0, df['DAP'].max()+10, 1))  # adjust the y tick frequency
    ax1.set_yticks([])
    
    
    v_lines = []
    v_lines_values = ','.join([str(x) for x in df['DAP'].unique()]).split(',')
    #print(len(ax1.get_xticklabels()))
    for label in ax1.get_xticklabels(): #minor=True
        if str(label.get_text()) in v_lines_values:
            #print(label.get_text())
            if (len(v_lines) < len(v_lines_values)):
                v_lines.append(label.get_position()[0])

    #print(v_lines, v_lines_values)
    #ax1.vlines(v_lines, 0, 1, ls='-.', color='lightgray', linewidth=0.75)
    ax1.set_xticks(v_lines) #ax1.get_xticks()[::len(v_lines_values)])
    ax1.tick_params(axis='x', labelsize=10, color='lightgray', rotation=90)
    # ------------
    
    #fig.suptitle('Sum of growing degree days since stage initiation', fontsize=18) #
    fig.suptitle('Phenological growth stages of Wheat', fontsize=18) #

    #fig.savefig(os.path.join(DATASET_IWIN_PATH, "Wheat_SUMDTT_GrowStages.png"))
    fig.tight_layout()
    plt.show()


# ------------------------------------
#  Functions to process IWIN dataset
# ------------------------------------
def plot_results_v3(df_tmp=None, xy_lim=40, xylim=False, clr1='b',clr2='r', clr3='black',s=5,alpha=0.2,
                                 e_threshold=10, h_threshold=15, a_threshold=10, m_threshold=10,
                                 rmoutliers=False, dispScore=True, dispBads=False, fgsize=(8,14), 
                                 title='Phenological stages of Wheat (IWIN)',
                                 saveFig=True, showFig=True, path_to_save_results='./', dirname='Figures', 
                                 fname='Fig_1_calibration_phenology_IWIN_locations', fmt='pdf'
                                ):

    def createFigure_v2(ax, data=None, code=(-1,1), stage='', v='DOY', fld1=None, fld2=None, 
                     xy_lim=40, clr1='g', clr2='r', clr3='black', s=10, alpha=0.2, 
                     dispScore=True, dispBads=False, xylim=True):
        df = data.copy()
        df.dropna(subset=[fld1,fld2], inplace=True)
        df_ok = df[df['status']==code[1]]
        df_outliers = df[df['status']==code[0]]
        df_outliers2 = df[df['status']==-99]
        ax.scatter(x=df_ok[fld1].to_numpy(), y=df_ok[fld2].to_numpy(), label=f'{stage} {v} (Wheat)', color=clr1, s=s, alpha=alpha )
        ax.scatter(x=df_outliers[fld1].to_numpy(), y=df_outliers[fld2].to_numpy(), label='Outliers', color=clr2, s=s, alpha=alpha, zorder=-1 )
        if (dispBads is True):
            ax.scatter(x=df_outliers2[fld1].to_numpy(), y=df_outliers2[fld2].to_numpy(), label='Outliers 2', color=clr3, s=s, alpha=alpha )
        ax.axline((0, 0), slope=1, color='#444', ls="-", linewidth=0.75, zorder=-2, label="line 1:1") #c=".5",
        #if (xylim is True):
        #    #maxlim = int(max(df[fld1].max(), df[fld2].max())) + xy_lim
        #    #ax.set(xlim=(0, maxlim), ylim=(0, maxlim))
        #    pass
        ax.set_xlabel(f"Observed {stage} ({v})")
        ax.set_ylabel(f"Simulated {stage} ({v})")
        ax.grid(visible=True, which='major', color='#d3d3d3', linewidth=0.25)
        ax.set_axisbelow(True)
        if (dispScore==True):
            try:
                r2score0, mape0, rmse0, n_rmse0, d_index0, ef0, accuracy0 = getScores(df, fld1=fld1, fld2=fld2)
                if (rmoutliers is True):
                    r2score, mape, rmse, n_rmse, d_index, ef, accuracy = getScores(df_ok, fld1=fld1, fld2=fld2)
                    ax.text(0.05,0.96,'Observations: {}\nRMSE: {:.1f} - [{:.1f}] days'.format(len(df), rmse0, rmse) + '\nNRMSE: {:.3f} - [{:.3f}]\nd-index: {:.2f} - [{:.2f}]\nR$^2$: {:.2f} - [{:.2f}]\nAccuracy: {:.2f}% - [{:.2f}%]'.format(n_rmse0, n_rmse, d_index0, d_index, 
                                                                                                                                                                                                                                           r2score0, r2score, accuracy0, accuracy), 
                             fontsize=8, ha='left', va='top', transform=ax.transAxes)
                else:
                    r2score, mape, rmse, n_rmse, d_index, ef, accuracy = getScores(df_ok, fld1=fld1, fld2=fld2)
                    #ax.text(0.05,0.96,'Observations: {}\nOutliers: {}\nRMSE: {:.1f}'.format(len(df), (len(df_outliers) + len(df_outliers2)), rmse) + '\nn-RMSE: {:.3f}\nd-index: {:.2f}\nR$^2$: {:.2f}\nAccuracy: {:.2f}%'.format(n_rmse, d_index, r2score, accuracy), 
                    #         fontsize=8, ha='left', va='top', transform=ax.transAxes)
                    ax.text(0.05,0.96,'Observations: {}\nOutliers: {}\nRMSE: {:.1f} - [{:.1f}] days'.format(len(df), (len(df_outliers) + len(df_outliers2)), rmse0, rmse) + '\nNRMSE: {:.3f} - [{:.3f}]\nd-index: {:.2f} - [{:.2f}]\nR$^2$: {:.2f} - [{:.2f}]\nAccuracy: {:.2f}% - [{:.2f}%]'.format(n_rmse0, n_rmse, d_index0, d_index, 
                                                                                                                                                                                                                                           r2score0, r2score, accuracy0, accuracy), 
                             fontsize=8, ha='left', va='top', transform=ax.transAxes)
            except Exception as err:
                #print("Problem getting metrics")
                pass

    # Create figures
    df = df_tmp.copy()
    fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4,2, figsize=fgsize)
    fig.subplots_adjust(top=0.9)

    # Mejorar la visualización de outliers
    df_final = pd.DataFrame()
    # Residuals
    if (('ObsEmergDOY' in df.columns) or ('ObsEmergDAP' in df.columns) ):
        # Figures 1
        df_final = pd.concat([df_final, df[df['status']==1]], axis=0)
        createFigure_v2(ax1, data=df, code=(-1,1), stage='Emergence', v='DOY', fld1="ObsEmergDOY", fld2="emerDOY", 
                     xy_lim=40, clr1='brown', clr2='b', s=s, alpha=alpha, dispScore=dispScore, dispBads=dispBads, xylim=True)
        # Figures 2
        createFigure_v2(ax2, data=df, code=(-1,1), stage='Emergence', v='DAP', fld1="ObsEmergDAP", fld2="emerDAP", 
                     xy_lim=40, clr1='brown', clr2='b', s=s, alpha=alpha, dispScore=dispScore, dispBads=dispBads, xylim=True)

    if (('ObsHeadingDOY' in df.columns) or ('ObsHeadingDAP' in df.columns)):
        # Figures 3 
        df_final = pd.concat([df_final, df[df['status']==2]], axis=0)
        createFigure_v2(ax3, data=df, code=(-2,2), stage='Heading', v='DOY', fld1="ObsHeadingDOY", fld2="headDOY", 
                     xy_lim=40, clr1='g', s=s, alpha=alpha, dispScore=dispScore, dispBads=dispBads, xylim=True)
        # Figures 4
        createFigure_v2(ax4, data=df, code=(-2,2), stage='Heading', v='DAP', fld1="ObsHeadingDAP", fld2="headDAP", 
                     xy_lim=40, clr1='g', s=s, alpha=alpha, dispScore=dispScore, dispBads=dispBads, xylim=True)

    if (('ObsAnthesisDOY' in df.columns) or ('ObsAnthesisDAP' in df.columns)):
        # Figures 5
        df_final = pd.concat([df_final, df[df['status']==3]], axis=0)
        createFigure_v2(ax5, data=df, code=(-3,3), stage='Anthesis', v='DOY', fld1="ObsAnthesisDOY", fld2="anthesisDOY", 
                     xy_lim=40, clr1='purple', s=s, alpha=alpha, dispScore=dispScore, dispBads=dispBads, xylim=True)
        # Figure 6
        createFigure_v2(ax6, data=df, code=(-3,3), stage='Anthesis', v='DAP', fld1="ObsAnthesisDAP", fld2="anthesisDAP", 
                     xy_lim=40, clr1='purple', s=s, alpha=alpha, dispScore=dispScore, dispBads=dispBads, xylim=True)

    if (('ObsMaturityDOY' in df.columns) or ('ObsMaturityDAP' in df.columns)):
        # Figures 7
        df_final = pd.concat([df_final, df[df['status']==4]], axis=0)
        createFigure_v2(ax7, data=df, code=(-4,4), stage='Maturity', v='DOY', fld1="ObsMaturityDOY", fld2="maturityDOY", 
                     xy_lim=40, clr1='orange', s=s, alpha=alpha, dispScore=dispScore, dispBads=dispBads, xylim=True)
        # Figures 8
        createFigure_v2(ax8, data=df, code=(-4,4), stage='Maturity', v='DAP', fld1="ObsMaturityDAP", fld2="maturityDAP", 
                     xy_lim=40, clr1='orange', s=s, alpha=alpha, dispScore=dispScore, dispBads=dispBads, xylim=True)

    fig.suptitle(f'{title}', fontsize=18) #
    fig.tight_layout()
    # Save in PDF
    hoy = dt.datetime.now().strftime('%Y%m%d')
    figures_path = os.path.join(path_to_save_results, '{}_{}'.format(dirname, hoy))
    if not os.path.isdir(figures_path):
        os.makedirs(figures_path)
    if (saveFig is True and fmt=='pdf'):
        fig.savefig(os.path.join(figures_path,"{}_{}.{}".format(fname, hoy, fmt)), 
                    bbox_inches='tight', orientation='portrait',  
                    edgecolor='none', transparent=False, pad_inches=0.5, dpi=300)

    if (saveFig==True and (fmt=='jpg' or fmt=='png')):
        fig.savefig(os.path.join(figures_path,"{}_{}.{}".format(fname, hoy, fmt)), 
                    bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none', transparent=False, dpi=300)

    #if (showFig is True):
    #    fig.show()
    #else:
    #    del fig
    #    plt.close();
    return fig, df_final


def correctStatus(df_tmp, e_threshold=4, h_threshold=10, a_threshold=5, m_threshold=10):
    ''' Add status '''
    df = df_tmp.copy()
    df['eresidualsDAP'] = df['ObsEmergDAP'] - df['emerDAP']
    df['eresidualsDOY'] = df['ObsEmergDOY'] - df['emerDOY']
    df['hresidualsDAP'] = df['ObsHeadingDAP'] - df['headDAP']
    df['hresidualsDOY'] = df['ObsHeadingDOY'] - df['headDOY']
    df['aresidualsDAP'] = df['ObsAnthesisDAP'] - df['anthesisDAP']
    df['aresidualsDOY'] = df['ObsAnthesisDOY'] - df['anthesisDOY']
    df['mresidualsDAP'] = df['ObsMaturityDAP'] - df['maturityDAP']
    df['mresidualsDOY'] = df['ObsMaturityDOY'] - df['maturityDOY']

    # for emergence 1 = good, -1 = bad
    #e_threshold=10
    #df['status'] = -1
    df.loc[( ((df["eresidualsDAP"]>= -e_threshold) & (df["eresidualsDAP"]<=e_threshold)) ), 'status'] = 1
    #df.loc[( ~((df["eresidualsDAP"]>= -e_threshold) & (df["eresidualsDAP"]<=e_threshold)) ), 'status'] = -1
    # Outliers
    df.loc[( (df['ObsEmergDOY']<150) & (df['emerDOY']>300) ), 'status'] = -99
    df.loc[( (df['ObsEmergDOY']>200) & (df['emerDOY']<150) ), 'status'] = -99
    df.loc[( (df['ObsEmergDAP']>80) & (df['emerDAP']>80) ), 'status'] = -1
    # Bad records
    df.loc[( (df['ObsEmergDAP']<=0) | (df['ObsEmergDAP']>50) ), 'status'] = -99
    
    # for heading 2 = good, -2 = bad
    #h_threshold=10
    #df['status'] = -2
    df.loc[( ~(df["eresidualsDAP"]<0) 
              & ((df["hresidualsDAP"] >= -h_threshold) & (df["hresidualsDAP"] <= h_threshold)) ), 'status'] = 2
    #df.loc[~( ~(df["eresidualsDAP"]<0) 
    #          & ((df["hresidualsDAP"] >= -h_threshold) & (df["hresidualsDAP"] <= h_threshold)) ), 'status'] = -2
    df.loc[( (df['ObsHeadingDAP']>250) | (df['ObsHeadingDAP']<0) ), 'status'] = -2
    df.loc[( (df['headDAP']>250) | (df['headDAP']<0) ), 'status'] = -2
    # Bad records
    df.loc[( (df['headDOY']>200) & (df['ObsHeadingDOY']<100) ), 'status'] = -99
    df.loc[( (df['ObsHeadingDOY']>200) & (df['headDOY']<100) ), 'status'] = -99
    df.loc[( (df['headDAP']>250) | (df['ObsHeadingDAP']>250) ), 'status'] = -99
    
    # for anthesis 3 = good, -3 = bad
    #a_threshold=10
    #df['status'] = -3
    df.loc[( ((df["aresidualsDAP"]>= -a_threshold) & (df["aresidualsDAP"]<=a_threshold)) ), 'status'] = 3
    #df.loc[( ~((df["aresidualsDAP"]>= -a_threshold) & (df["aresidualsDAP"]<=a_threshold)) ), 'status'] = -3
    # Outliers
    df.loc[( (df['anthesisDAP']>300) ), 'status'] = -3
    # Bad records
    df.loc[( (df['ObsAnthesisDAP']>300) | (df['ObsAnthesisDAP']<0) ), 'status'] = -99
    
    # for anthesis 4 = good, -4 = bad
    #m_threshold=10
    #df['status'] = -4
    df.loc[( ((df["mresidualsDAP"]>= -m_threshold) & (df["mresidualsDAP"] <= m_threshold)) ), 'status'] = 4
    #df.loc[( ~((df["mresidualsDAP"]>= -m_threshold) & (df["mresidualsDAP"] <= m_threshold)) ), 'status'] = -4
    # Outliers
    df.loc[( (df['maturityDAP']>350) ), 'status'] = -4
    df.loc[( (df['ObsMaturityDOY']>300) & (df['maturityDOY']<100) ), 'status'] = -99
    # Bad records
    df.loc[( (df['ObsMaturityDAP']>350) | (df['ObsMaturityDAP']<0) ), 'status'] = -99
    df.loc[( (df['maturityDAP']>350) | (df['maturityDAP']<0) ), 'status'] = -99
    
    print(df['status'].value_counts())

    return df

def correctStatus_v2(df_tmp, e_threshold=4, h_threshold=10, a_threshold=5, m_threshold=10):
    ''' Add status '''
    df = df_tmp.copy()
    df['eresidualsDAP'] = df['ObsEmergDAP'] - df['emerDAP']
    df['eresidualsDOY'] = df['ObsEmergDOY'] - df['emerDOY']
    df['hresidualsDAP'] = df['ObsHeadingDAP'] - df['headDAP']
    df['hresidualsDOY'] = df['ObsHeadingDOY'] - df['headDOY']
    df['aresidualsDAP'] = df['ObsAnthesisDAP'] - df['anthesisDAP']
    df['aresidualsDOY'] = df['ObsAnthesisDOY'] - df['anthesisDOY']
    df['mresidualsDAP'] = df['ObsMaturityDAP'] - df['maturityDAP']
    df['mresidualsDOY'] = df['ObsMaturityDOY'] - df['maturityDOY']

    df_copy = df.copy()
    # for emergence 1 = good, -1 = bad
    df['status'] = -1
    df.loc[( ((df["eresidualsDAP"]>= -e_threshold) & (df["eresidualsDAP"]<=e_threshold)) ), 'status'] = 1
    #df.loc[( ~((df["eresidualsDAP"]>= -e_threshold) & (df["eresidualsDAP"]<=e_threshold)) ), 'status'] = -1
    # Outliers
    df.loc[( (df['ObsEmergDOY']<150) & (df['emerDOY']>300) ), 'status'] = -99
    df.loc[( (df['ObsEmergDOY']>200) & (df['emerDOY']<150) ), 'status'] = -99
    df.loc[( (df['ObsEmergDAP']>80) & (df['emerDAP']>80) ), 'status'] = -1
    # Bad records
    df.loc[( (df['ObsEmergDAP']<=0) | (df['ObsEmergDAP']>50) ), 'status'] = -99
    # save 
    df_e = df.copy()
    
    # for heading 2 = good, -2 = bad
    df = df_copy.copy()
    df['status'] = -2
    df.loc[( ~(df["eresidualsDAP"]<0) 
              & ((df["hresidualsDAP"] >= -h_threshold) & (df["hresidualsDAP"] <= h_threshold)) ), 'status'] = 2
    #df.loc[~( ((df["hresidualsDAP"] >= -h_threshold) & (df["hresidualsDAP"] <= h_threshold)) ), 'status'] = -2
    df.loc[( (df['ObsHeadingDAP']>250) | (df['ObsHeadingDAP']<0) ), 'status'] = -2
    df.loc[( (df['headDAP']>250) | (df['headDAP']<0) ), 'status'] = -2
    # Bad records
    df.loc[( (df['headDOY']>200) & (df['ObsHeadingDOY']<100) ), 'status'] = -99
    df.loc[( (df['ObsHeadingDOY']>200) & (df['headDOY']<100) ), 'status'] = -99
    df.loc[( (df['headDAP']>250) | (df['ObsHeadingDAP']>250) ), 'status'] = -99
    # save 
    df_h = df.copy()
    
    # for anthesis 3 = good, -3 = bad
    df = df_copy.copy()
    df['status'] = -3
    df.loc[( ((df["aresidualsDAP"]>= -a_threshold) & (df["aresidualsDAP"]<=a_threshold)) ), 'status'] = 3
    #df.loc[~( ((df["aresidualsDAP"]>= -a_threshold) & (df["aresidualsDAP"]<=a_threshold)) ), 'status'] = -3
    # Outliers
    df.loc[( (df['anthesisDAP']>300) ), 'status'] = -99
    # Bad records
    df.loc[( (df['ObsAnthesisDAP']>300) | (df['ObsAnthesisDAP']<0) ), 'status'] = -99
    # save 
    df_a = df.copy()
    
    # for anthesis 4 = good, -4 = bad
    df = df_copy.copy()
    df['status'] = -4
    df.loc[( ((df["mresidualsDAP"]>= -m_threshold) & (df["mresidualsDAP"] <= m_threshold)) ), 'status'] = 4
    #df.loc[( ~((df["mresidualsDAP"]>= -m_threshold) & (df["mresidualsDAP"] <= m_threshold)) ), 'status'] = -4
    # Outliers
    df.loc[( (df['maturityDAP']>350) ), 'status'] = -4
    # Bad records
    df.loc[( (df['ObsMaturityDAP']>350) | (df['ObsMaturityDAP']<0) ), 'status'] = -99
    df.loc[( (df['maturityDAP']>350) | (df['maturityDAP']<0) ), 'status'] = -99
    # save 
    df_m = df.copy()

    df = pd.concat([df_e, df_h, df_a, df_m], axis=0, ignore_index=True)
    
    print(df['status'].value_counts())

    return df



def estimatePhenologicalStages_InParallel(fname='IWIN', sites_to_run=None, batch_size=1000, n_jobs=-2, 
                                          useDefault=True, useBruteForce=False, e_threshold=10, h_threshold=15, a_threshold=10, 
                                          m_threshold=10, rmoutliers=False, 
                                          saveIntermediateFiles=False, saveFile=True, vb=False):
    '''
        Estimate phenological stages of wheat running simulations in Parallel
        
        Parameters:
            sites_to_run (array): Array of Site objects

        Returns: 
            An array of sites with intermediate results

    '''
    if (sites_to_run is None):
        print("Model parameters not valid")
        return
    hoy = dt.datetime.now().strftime('%Y%m%d')
    nObs = len(sites_to_run)
    step = np.ceil(nObs / batch_size)
    if (vb is True):
        print("Number of Obs:{} - in {:.0f} steps, using batch size: {}".format(nObs, step, batch_size))
    df = None
    # Run in parallel
    for b in range(int(step)):
        part = b + 1
        batch_start= b * batch_size
        batch_end = (b+1) * batch_size
        if (vb is True):
            print("Batch {} - from {} to {}".format(part, batch_start, batch_end))
        processed_parcels_df = estimatePhenologicalStages_InBatch(fname=fname, sites_to_run=sites_to_run, 
                                                                    batch_start=batch_start, batch_end=batch_end, n_jobs=n_jobs, 
                                                                    useDefault=useDefault, useBruteForce=useBruteForce,
                                                                    fmt="parquet", saveFile=saveIntermediateFiles, 
                                                                    verbose=False)
        df = pd.concat([df, processed_parcels_df])
    
    # update some features
    try:
        #df.drop(columns=['bruteforce', 'sowing_date', 'latitude', 'longitude'], inplace=True)
        df['errors'] = df['errors'].astype(str)
        df['sowing'] = pd.to_datetime(df['sowing'].astype(str), format='%Y-%m-%d')
        df['emerDATE'] = pd.to_datetime(df['emerDATE'].astype(str), format='%Y-%m-%d')
        df['headDATE'] = pd.to_datetime(df['headDATE'].astype(str), format='%Y-%m-%d')
        df['anthesisDATE'] = pd.to_datetime(df['anthesisDATE'].astype(str), format='%Y-%m-%d')
        df['maturityDATE'] = pd.to_datetime(df['maturityDATE'].astype(str), format='%Y-%m-%d')

        # Outliers
        df = correctStatus(df, e_threshold=e_threshold, h_threshold=h_threshold, 
                           a_threshold=a_threshold, m_threshold=m_threshold)

    except Exception as err:
        print("Problem processing dataframe results.", err)
    #
    #
    print("Phenology stages were estimated successfully!")
    # Save all values
    hoy = dt.datetime.now().strftime('%Y%m%d')
    out_path = os.path.join( RESULT_PATH, f"{fname}_Pheno_parts_{hoy}")
    if not os.path.isdir(out_path):
        os.makedirs(out_path, exist_ok=True)
    #if (saveIntermediateFiles is False):
    #    mergedfname = f"{fname}_calibratedPhenology_merged_{hoy}.parquet"
    #    res_path = RESULT_PATH + '../'
    #    mergeParquetFiles(res_path, out_path, fname=mergedfname, removeParts=True)
    
    if (saveFile is True):
        try:
            df.to_parquet(os.path.join(out_path, f"{fname}_calibratedPhenology_{hoy}.parquet"), 
                          index=False, compression=None)
        except Exception as err:
            print("Problem saving final results. Error:", err)
    #
    return df

def estimatePhenologicalStages_InBatch(fname='IWIN', sites_to_run=None, batch_start=0, batch_end=1000, n_jobs=-2,
                                       useDefault=True, useBruteForce=False, fmt="parquet", saveFile=True, verbose=False):
    '''
        Estimate phenological stages of wheat for each observation running model in Parallel

        Parameters:
            sites_to_run (array): Array of Site objects

        Returns: 
            An array of sites with intermediate results

    '''
    if (sites_to_run is None):
        print("Model parameters not valid")
        return
    output = []
    with Parallel(n_jobs=n_jobs, verbose=5) as parallel:
        delayed_funcs = [delayed(lambda s: process_Phenology_Stages(s, useDefault, useBruteForce, verbose))(run) 
                         for run in sites_to_run[batch_start:batch_end]]
        output = parallel(delayed_funcs)
    #print(output)
    #df = pd.DataFrame(output)
    processed_parcels_df = pd.DataFrame(output)
    #processed_parcels_df.drop(columns=['errors'], inplace=True)
    processed_parcels_df.reset_index(drop=True, inplace=True)
    if (saveFile is True):
        try:
            # Save in binary format
            hoy = dt.datetime.now().strftime('%Y%m%d')
            out_path = os.path.join( RESULT_PATH, f"{fname}_Pheno_parts_{hoy}")
            if not os.path.isdir(out_path):
                os.makedirs(out_path, exist_ok=True)
            if (fmt=="parquet"):
                processed_parcels_df.to_parquet(os.path.join(out_path, f"{fname}_Pheno_{hoy}_part{batch_start}_{batch_end}.parquet"), 
                                                index=False, compression=None)
            elif (fmt=="csv"):
                    processed_parcels_df.to_csv(os.path.join(out_path, f"{fname}_Pheno_{hoy}_part{batch_start}_{batch_end}.csv"),
                                                index=False)
        except Exception as err:
            print("Problem saving intermediate files. Error:", err)
    output = None
    del output
    _ = gc.collect()
    return processed_parcels_df


def process_Phenology_Stages(s, useDefault, useBruteForce, verbose):
    global config
    global Weather
    
    # Update params
    def update_stiteParams(s, params):
        obsEmerDAP = None
        obsHeadDAP = None
        obsAnthesisDAP = None
        obsMaturityDAP = None
        if ('ObsEmergDAP' in s[0]['attributes']):
            try:
                obsEmerDAP = int(s[0]['attributes']['ObsEmergDAP'])
                # Not run bad observations
                if ((obsEmerDAP < 0) or (obsEmerDAP > 100)):
                    print("DAP not valid for Emergence")
                    obsEmerDAP = None
            except Exception as err:
                obsEmerDAP = None
        else:
            obsEmerDAP = None

        if ('ObsHeadingDAP' in s[0]['attributes']):
            try:
                obsHeadDAP = int(s[0]['attributes']['ObsHeadingDAP'])
                if ((obsHeadDAP < 0) and (obsHeadDAP > 220)):
                    print("DAP not valid for Heading")
                    obsHeadDAP = None
            except Exception as err:
                obsHeadDAP = None
        else:
            obsHeadDAP = None

        if ('ObsAnthesisDAP' in s[0]['attributes']):
            try:
                obsAnthesisDAP = int(s[0]['attributes']['ObsAnthesisDAP'])
                if ((obsAnthesisDAP < 0) and (obsAnthesisDAP > 350)):
                    print("DAP not valid for Anthesis")
                    obsAnthesisDAP = None
            except Exception as err:
                obsAnthesisDAP = None
        else:
            obsAnthesisDAP = None

        if ('ObsMaturityDAP' in s[0]['attributes']):
            try:
                obsMaturityDAP = int(s[0]['attributes']['ObsMaturityDAP'])
                if ((obsMaturityDAP < 0) and (obsMaturityDAP > 350)):
                    print("DAP not valid for Maturity")
                    obsMaturityDAP = None
            except Exception as err:
                obsMaturityDAP = None
        else:
            obsMaturityDAP = None

        #
        # Update variables 
        update_params = dict(
            bruteforce = False,
            brute_params = {
                        "obsEmergenceDAP": obsEmerDAP, # Observed days after planting to emergence.
                        "obsHeadingDAP": obsHeadDAP, # Observed days after planting to heading.
                        "obsAnthesisDAP": obsAnthesisDAP, # Observed days after planting to Anthesis.
                        "obsMaturityDAP": obsMaturityDAP, # Observed days after planting to Maturity.
                        "max_tries": 500, # Number of maximum tries to find the best value
                        "error_lim": 0.5, # Threshold to classify the observation as a good or bad
                        "gdde_steps": 1.0, # Step to increase or reduce the GDDE parameters. Default 1.0
                        "maxGDDE": 100, #Threshold for the maximum value of GDDE to reach emergence date
                        "phint_steps": 1.0, # Step to increase or reduce the PHINT parameters. Default 1.0
                        "maxPHINT": 150, #Threshold for the maximum value of PHINT to reach heading date
                        "adap_steps": 1, #Step to increase or reduce the ADAH parameters. Default 1.0
                        "maxADAP": 10, #Threshold for the maximum value of ADAH to reach anthesis date.
                        "p5_steps": 1, #Step to increase or reduce the P5 parameters. Default 1.0
                        "maxP5": 3000 #Threshold for the maximum value of P5 to reach anthesis date.
                    },
        )
        params = {**params,**update_params}

        return params

    try:
        status = 1
        attrs = s['attributes']
        loc = attrs['location']
        country = attrs['country']
        occ = attrs['Occ']
        E = attrs['E']
        G = attrs['G']
        #month = attrs['month']
        sowingdate = attrs['sowing']
        lat = float(attrs['lat'])
        lon = float(attrs['lon'])
        genotype = attrs['genotype']
        filter_weather_data = Weather[((Weather['location']==loc) & (Weather['DATE']>=sowingdate) )]
        
        # Initialization of variables 
        params = dict(
            weather = filter_weather_data,
            sowing_date = sowingdate, # Sowing date in YYYY-MM-DD
            latitude = lat, # Latitude of the site
            longitude = lon, # Longitude of the site
            genotype = genotype, # Name of the grand parent in IWIN pedigrees database #eg. LOCAL CHECK, FRANCOLIN #1
            SNOW = attrs['SNOW'], #0, # Snow fall
            SDEPTH = attrs['SDEPTH'], #3.0, # Sowing depth in cm
            GDDE = attrs['GDDE'], #6.2, # Growing degree days per cm seed depth required for emergence, GDD/cm
            DSGFT = attrs['DSGFT'], #200, # GDD from End Ear Growth to Start Grain Filling period
            VREQ  = attrs['VREQ'], #505.0, # Vernalization required for max.development rate (VDays)
            PHINT = attrs['PHINT'], #95.0, # Phyllochron. A good estimate for PHINT is 95 degree days. This value for PHINT is appropriate except for spring sown wheat in latitudes greater than 30 degrees north and 30 degrees south, in which cases a value for PHINT of 75 degree days is suggested. 
            P1V = attrs['P1V'], #1.0, # development genetic coefficients, vernalization. 1 for spring type, 5 for winter type
            P1D = attrs['P1D'], #3.675, # development genetic coefficients, Photoperiod (1 - 6, low- high sensitive to day length)
            P5 = attrs['P5'], #500, # grain filling degree days eg. 500 degree-days. Old value was divided by 10.
            P6 = attrs['P6'], #250, # approximate the thermal time from physiological maturity to harvest
            DAYS_GERMIMATION_LIMIT = 40, # threshold for days to germination
            TT_EMERGENCE_LIMIT = 800, # threshold for thermal time to emergence
            TT_TDU_LIMIT = 400, # threshold for thermal development units (TDU),
            ADAH = attrs['ADAH'], #6, # threshold for anthesis date after planting. This is a 6 days after heading.
            bruteforce = False,
            brute_params = {
                        "obsEmergenceDAP": attrs['ObsEmergDAP'], # Observed days after planting to emergence.
                        "obsHeadingDAP": attrs['ObsHeadingDAP'], # Observed days after planting to heading.
                        "obsAnthesisDAP": attrs['ObsAnthesisDAP'], # Observed days after planting to Anthesis.
                        "obsMaturityDAP": attrs['ObsMaturityDAP'], # Observed days after planting to Maturity.
                        "max_tries": 500, # Number of maximum tries to find the best value
                        "error_lim": 0.5, # Threshold to classify the observation as a good or bad
                        "gdde_steps": 1.0, # Step to increase or reduce the GDDE parameters. Default 1.0
                        "maxGDDE": 100, #Threshold for the maximum value of GDDE to reach emergence date
                        "phint_steps": 1.0, # Step to increase or reduce the PHINT parameters. Default 1.0
                        "maxPHINT": 150, #Threshold for the maximum value of PHINT to reach heading date
                        "adap_steps": 1, #Step to increase or reduce the ADAH parameters. Default 1.0
                        "maxADAP": 10, #Threshold for the maximum value of ADAH to reach anthesis date.
                        "p5_steps": 1, #Step to increase or reduce the P5 parameters. Default 1.0
                        "maxP5": 5000 #Threshold for the maximum value of P5 to reach anthesis date.
                    }
        )
        
        # Get Emergence by brute force
        #growstages, params, status = estimate_emergence_by_bruteforce(params)
        
        # Get Heading by brute force
        #growstages, params, status = estimate_heading_by_bruteforce(params)

        # Get Anthesis by brute force
        #growstages, params, status = estimate_anthesis_by_bruteforce(params)

        # Get Maturity by brute force
        #growstages, params, status = estimate_maturity_by_bruteforce_v2(params)

        
        growstages, params = determine_phenology_stages(config=config, initparams=params, useDefault=True, 
                                                        dispDates=False, dispFigPhenology=False)
        #
        del params['weather'], params['brute_params']
        if ((growstages is not None) and (growstages['2']['DOY']!='') and (growstages['2.5']['DOY']!='') ):
            result = {**params,**{
                                  'emerDATE':growstages['9']['date'], 
                                  'emerDOY':growstages['9']['DOY'], 'emerDAP':growstages['9']['DAP'],
                                  'emerAGE':growstages['9']['AGE'], 'emerSUMDTT':growstages['9']['SUMDTT'],
                                  'headDATE':growstages['2']['date'],
                                  'headDOY':growstages['2']['DOY'], 'headDAP':growstages['2']['DAP'],
                                  'headAGE':growstages['2']['AGE'], 'headSUMDTT':growstages['2']['SUMDTT'],
                                  'anthesisDATE':growstages['2.5']['date'],
                                  'anthesisDOY':growstages['2.5']['DOY'], 'anthesisDAP':growstages['2.5']['DAP'],
                                  'anthesisAGE':growstages['2.5']['AGE'], 'anthesisSUMDTT':growstages['2.5']['SUMDTT'],
                                  'maturityDATE':growstages['5']['date'],
                                  'maturityDOY':growstages['5']['DOY'], 'maturityDAP':growstages['5']['DAP'],
                                  'maturityAGE':growstages['5']['AGE'], 'maturitySUMDTT':growstages['5']['SUMDTT'],
                                  'QC_status':status
                                 } }
            #
            s['attributes']['errors']=""
            s['attributes'] = {**attrs,**result}
    
    except Exception as err:
        print(f"Problem in observation GID: {s['attributes']['UID']}.",err)
        s['attributes']['errors']=str(err) #{"UID":s['attributes']['UID'], "error":err}
    
    #
    return s['attributes']
    
# ------------------------------------
#

#
# ------------------------------------
#
# ------------------------------------
#
# ------------------------------------
# Updated Sim for Loc-Occ-Yr
# ------------------------------------

def getTraitDay(sw, ndays):
    try:
        d = sw + pd.DateOffset(days=int(ndays))
        return d
    except:
        return np.nan
    
def getAnthesisMaturityDAP(df):
    '''Get Simulated Anthesis days after planting'''
    ADAP = np.nan
    MDAP = np.nan
    PDAT = str(df['PDAT'])
    ADAT = str(df['ADAT'])
    MDAT = str(df['MDAT'])
    if (PDAT!='nan' and PDAT!='-99' and ADAT!='nan' and ADAT!='-99' and MDAT!='nan' and MDAT!='-99'):
        #year,julian = [int(PDAT[:4]), int(PDAT[-3:])]
        f1 = dt.datetime(int(PDAT[:4]), 1, 1)+dt.timedelta(days=int(PDAT[-3:]) - 1)
        f2 = dt.datetime(int(ADAT[:4]), 1, 1)+dt.timedelta(days=int(ADAT[-3:]) - 1)
        f3 = dt.datetime(int(MDAT[:4]), 1, 1)+dt.timedelta(days=int(MDAT[-3:]) - 1)
        ADAP = (f2 - f1).days
        MDAP = (f3 - f1).days
        
    return ADAP, MDAP

def getAnthesisMaturityDAPv2(df, HDAP2AD=10):
    '''Get Simulated Anthesis days after planting'''
    ADAP = np.nan
    MDAP = np.nan
    HeadingDAP = np.nan
    PDAT = str(df['PDAT'])
    ADAT = str(df['ADAT'])
    MDAT = str(df['MDAT'])
    if (PDAT!='nan' and PDAT!='-99' and ADAT!='nan' and ADAT!='-99' and MDAT!='nan' and MDAT!='-99'):
        #year,julian = [int(PDAT[:4]), int(PDAT[-3:])]
        f1 = dt.datetime(int(PDAT[:4]), 1, 1)+dt.timedelta(days=int(PDAT[-3:]) - 1)
        f2 = dt.datetime(int(ADAT[:4]), 1, 1)+dt.timedelta(days=int(ADAT[-3:]) - 1)
        f3 = dt.datetime(int(MDAT[:4]), 1, 1)+dt.timedelta(days=int(MDAT[-3:]) - 1)
        ADAP = (f2 - f1).days
        MDAP = (f3 - f1).days
        HeadingDAP = int(ADAP) - HDAP2AD
    return ADAP, MDAP, HeadingDAP

def createWHX_simpleversion(df, byCultivar=False, allYrs=True, output_file=None):
    if (output_file is None):
        print("Input file not valid")
        return False
    people='GIRON, E., SCHULTHESS, U., PEQUENO, D.'
    hoy = dt.date.today().strftime('%Y-%m-%d')
    country = df.iloc[0]['country']
    location = df.iloc[0]['location']
    loc_desc = df.iloc[0]['locationname']
    loc_code = df.iloc[0]['loc_code']
    sowing = df.iloc[0]['sowing']
    # To adjust Grain Yield
    # PLANTING DETAILS and FERTILIZERS (INORGANIC)
    PPOP = 260 #300
    PPOE = 260 #300
    FAMN = 60  #120
    if (allYrs is True):
        YYDOY = "79{:03d}".format(int(df.iloc[0]['sowing'].strftime('%j')))
        SDATE = 79001
        EDATE = 79365
        NYERS = 40
    else:
        Y = int(df.iloc[0]['sowing'].strftime('%Y'))
        YY = str(Y)[-2:]
        DOY = int(df.iloc[0]['sowing'].strftime('%j'))
        YYDOY = "{:2}{:03d}".format(YY, DOY)
        SDATE = YYDOY #f"{YY}001"
        EDATE = "{:2}{:03d}".format(int(YY)+1, DOY) #f"{YY}365"
        NYERS = 1
        #print(Y, YY, DOY, SDATE, EDATE, NYERS)
    #
    
    # WHA file
    createWHA(df, output_file=output_file.replace('.WHX', '.WHA'))
    
    # WHX file
    header = f"""*EXP.DETAILS: CIMMYT IWIN Project 2022 - 2024                                  

*GENERAL
@PEOPLE
{people}
@ADDRESS
-99
@SITE
{location} - {loc_desc.title()}, {country.upper()}
@ PAREA  PRNO  PLEN  PLDR  PLSP  PLAY HAREA  HRNO  HLEN  HARM.........
    -99   -99   -99   -99   -99   -99   -99   -99   -99   -99

@NOTES 
FileX created automatically by egiron. Last updated: {hoy}

*TREATMENTS                        -------------FACTOR LEVELS------------
@N R O C TNAME.................... CU FL SA IC MP MI MF MR MC MT ME MH SM
"""
    
    soil = f"""*SOIL ANALYSIS
@A SADAT  SMHB  SMPX  SMKE  SANAME
 1 {YYDOY}   -99   -99   -99  -99                      
@A  SABL  SADM  SAOC  SANI SAPHW SAPHB  SAPX  SAKE  SASC
 1   -99   -99   -99   -99   -99   -99   -99   -99   -99
"""
    
    init_conditions = f"""*INITIAL CONDITIONS
@C   PCR ICDAT  ICRT  ICND  ICRN  ICRE  ICWD ICRES ICREN ICREP ICRIP ICRID ICNAME
! 1    WH {YYDOY}  1000   -99     1     1   -99  3000   -99   -99   -99   -99 HC_02    
 1    WH {YYDOY}  1200     0     1     1   -99  6500  1.14     0   100    15 -99
@C  ICBL  SH2O  SNH4  SNO3
 1    10     0   0.3     3
 1    15  .205   3.4   9.8
 1    30   .17   3.2   7.3
 1    60  .092   2.5   5.1
 1    90  .065   2.2   4.7
 1   120  .066   2.7   4.3
 1   150  .066   2.7   4.3
 1   180  .066   2.7   4.3
"""
    
    irrigation = f"""*IRRIGATION AND WATER MANAGEMENT
@I  EFIR  IDEP  ITHR  IEPT  IOFF  IAME  IAMT IRNAME
 1     1    30    50   100 GS000 IR001    10 Rainfed 20 mm       
@I IDATE  IROP IRVAL
 1     1 IR004    20
"""
    
    irrig_2 = f"""!*IRRIGATION AND WATER MANAGEMENT
!@I  EFIR  IDEP  ITHR  IEPT  IOFF  IAME  IAMT IRNAME
! 1     0   -99   -99   -99   -99   -99   -99 -99
!@I IDATE  IROP IRVAL
! 1 82096 IR001    65
! 1 82110 IR001    78
! 1 82117 IR001    70
"""

    fertilizers = """*FERTILIZERS (INORGANIC)
@F FDATE  FMCD  FACD  FDEP  FAMN  FAMP  FAMK  FAMC  FAMO  FOCD FERNAME
 1     0 FE001 AP004     5     0   -99   -99   -99   -99   -99 0-40-DAP            
 2    40 FE001 AP004     5   {:3}   -99   -99   -99   -99   -99 0-40-DAP  
""".format(FAMN)
    
    fert_2 = """*FERTILIZERS (INORGANIC)
@F FDATE  FMCD  FACD  FDEP  FAMN  FAMP  FAMK  FAMC  FAMO  FOCD FERNAME
! 1 81329 FE001 AP004     5     0     0     0     0     0   -99 -99
! 2 81329 FE001 AP004     5    60     0     0     0     0   -99 -99
! 3 81329 FE001 AP004     5    90     0     0     0     0   -99 -99
! 3 82056 FE001 AP004     1    90     0     0     0     0   -99 -99
"""

    residues = f"""*RESIDUES AND ORGANIC FERTILIZER
@R RDATE  RCOD  RAMT  RESN  RESP  RESK  RINP  RDEP  RMET RENAME
 1 {YYDOY}   -99   -99   -99   -99   -99   -99   -99   -99 -99                 
"""

    environment = f"""*ENVIRONMENT MODIFICATIONS
@E ODATE EDAY  ERAD  EMAX  EMIN  ERAIN ECO2  EDEW  EWIND ENVNAME
 1 {YYDOY} A   0 A   0 A   0 A   0 A 0.0 R 362 A   0 A   0 baseline            
"""

    harvest = f"""*HARVEST DETAILS
@H HDATE  HSTG  HCOM HSIZE   HPC  HBPC HNAME
 1 {YYDOY} GS000   -99   -99   -99   -99 DAP    
"""
    
    simulation = f"""*SIMULATION CONTROLS
@N GENERAL     NYERS NREPS START SDATE RSEED SNAME.................... SMODEL
 1 GE              {NYERS}     1     S {SDATE}  3417 SIM CONTR - IRRIGATED           
@N OPTIONS     WATER NITRO SYMBI PHOSP POTAS DISES  CHEM  TILL   CO2
 1 OP              Y     Y     N     N     N     N     N     N     M
@N METHODS     WTHER INCON LIGHT EVAPO INFIL PHOTO HYDRO NSWIT MESOM MESEV MESOL
 1 ME              M     M     E     R     S     C     R     1     G     S     2
@N MANAGEMENT  PLANT IRRIG FERTI RESID HARVS
 1 MA              R     A     D     N     M
@N OUTPUTS     FNAME OVVEW SUMRY FROPT GROUT CAOUT WAOUT NIOUT MIOUT DIOUT VBOSE CHOUT OPOUT FMOPT
 1 OU              N     Y     Y     1     Y     N     N     N     N     N     N     N     Y     C
"""
    
    automgnt = f"""@  AUTOMATIC MANAGEMENT
@N PLANTING    PFRST PLAST PH2OL PH2OU PH2OD PSTMX PSTMN
 1 PL          {SDATE} {SDATE}    40   100    30    40    10
@N IRRIGATION  IMDEP ITHRL ITHRU IROFF IMETH IRAMT IREFF
 1 IR             30    80   100 GS000 IR001    10     1
@N NITROGEN    NMDEP NMTHR NAMNT NCODE NAOFF
 1 NI             30    50    25 FE001 GS000
@N RESIDUES    RIPCN RTIME RIDEP
 1 RE            100     1    20
@N HARVEST     HFRST HLAST HPCNP HPCNR
 1 HA              0 {EDATE}   100     0
"""
    
    with open(output_file, 'w', encoding='cp1252', newline='\r\n' ) as f:
        f.writelines(header)
        # TREATMENTS
        N = 1
        for idx in df.index:
            N = idx + 1
            #TNAME = df['genotype'][idx][:25].replace('(','').replace(')','')
            #TNAME = str('GID' + str(df['GID'][idx]).replace('(','').replace(')','') + ' - ' + df['loc_code'][idx])[:25]
            TNAME = df['E'][idx][:25].replace('(','').replace(')','')
            if (byCultivar is False):
                f.writelines("""{:2} 1 1 0 {:25}  1  1  0  1  1  1  1  0  0  0  0  0  1\n""".format(N, TNAME, N, N ))
            else:
                f.writelines("""{:2} 1 1 0 {:25} {:2} {:2}  0  1 {:2}  1  1  0  0  0  0  0  1\n""".format(N, TNAME, N, N, N ))
        # CULTIVARS
        f.writelines("\r\n")
        f.writelines("*CULTIVARS\n")
        f.writelines("@C CR INGENO CNAME\n")
        if (byCultivar is True):
            for idx in df.index:
                C = idx + 1
                INGENO = df.iloc[idx]['INGENO'][:6]
                CNAME = df.iloc[idx]['CNAME'][:16]
                f.writelines("{:2} WH {:6} {:16}\n".format(C, INGENO, CNAME))
        else:
            C = 1
            INGENO = df.iloc[0]['INGENO'][:6]
            CNAME = df.iloc[0]['CNAME'][:16]
            f.writelines("{:2} WH {:6} {:16}\n".format(C, INGENO, CNAME))
        #
        f.writelines("\r\n")
        f.writelines("*FIELDS\n")
        f.writelines("@L ID_FIELD WSTA....  FLSA  FLOB  FLDT  FLDD  FLDS  FLST SLTX  SLDP  ID_SOIL    FLNAME\n")
        if (byCultivar is True):
            for idx in df.index:
                L = idx + 1
                ID_FIELD = 'FIELD' + str("{:03d}".format(L))
                WSTA = df.iloc[idx]['WSTA'][:8]
                ID_SOIL = df.iloc[idx]['ID_SOIL'][:10]
                FLNAME = df.iloc[idx]['genotype'][:25].replace('(','').replace(')','')
                f.writelines("{:2} {:8} {:8}   -99   -99   -99   -99   -99   -99  -99   -99  {:10} {:25} \n".format(L, ID_FIELD, WSTA, ID_SOIL, FLNAME))
        else:
            L = 1
            ID_FIELD = 'FIELD' + str("{:03d}".format(L))
            WSTA = df.iloc[0]['WSTA'][:8]
            ID_SOIL = df.iloc[0]['ID_SOIL'][:10]
            FLNAME = df.iloc[0]['locationname'][:25].replace('(','').replace(')','')
            #FLNAME = df.iloc[0]['GID'][:25]
            f.writelines("{:2} {:8} {:8}   -99   -99   -99   -99   -99   -99  -99   -99  {:10} {:25} \n".format(L, ID_FIELD, WSTA, ID_SOIL, FLNAME))
        #
        f.writelines("@L ...........XCRD ...........YCRD .....ELEV .............AREA .SLEN .FLWR .SLAS FLHST FHDUR\n")
        if (byCultivar is True):
            for idx in df.index:
                L = idx + 1
                XCRD = str(df.iloc[idx]['lon'])[:15]
                YCRD = str(df.iloc[idx]['lat'])[:15]
                f.writelines("{:2} {:>15} {:>15}       -99               -99   -99   -99   -99   -99   -99\n".format(L, XCRD, YCRD))
        else:
            L = 1
            XCRD = str(df.iloc[0]['lon'])[:15]
            YCRD = str(df.iloc[0]['lat'])[:15]
            f.writelines("{:2} {:>15} {:>15}       -99               -99   -99   -99   -99   -99   -99\n".format(L, XCRD, YCRD))
        #
        # SOIL ANALYSIS
        f.writelines("\r\n")
        f.writelines(soil)
        #
        # INITIAL CONDITIONS
        f.writelines("\r\n")
        f.writelines(init_conditions)
        # 
        # PLANTING DETAILS
        f.writelines("\r\n")
        f.writelines("*PLANTING DETAILS\n")
        f.writelines("@P PDATE EDATE  PPOP  PPOE  PLME  PLDS  PLRS  PLRD  PLDP  PLWT  PAGE  PENV  PLPH  SPRL                        PLNAME\n")
        if (byCultivar is True):
            for idx in df.index:
                P = idx + 1
                #PDATE = YYDOY  #df.iloc[idx]['sowing'].strftime('%Y%j')[-5:]
                #f.writelines("{:2} {:5}   -99   {:3}   {:3}     S     R   -99     5     5   -99   -99   -99   -99   -99\n".format(P, YYDOY, PPOP, PPOE))
                f.writelines("{:2} {:5}   -99   {:3}   {:3}     S     R   -99     5     5   -99   -99   -99   -99   -99                        -99\n".format(P, YYDOY, PPOP, PPOE))
        else:
            P = 1
            #f.writelines("{:2} {:5}   -99   {:3}   {:3}     S     R   -99     5     5   -99   -99   -99   -99   -99\n".format(P, YYDOY, PPOP, PPOE))
            f.writelines("{:2} {:5}   -99   {:3}   {:3}     S     R   -99     5     5   -99   -99   -99   -99   -99                        -99\n".format(P, YYDOY, PPOP, PPOE))
        # 
        # IRRIGATION AND WATER MANAGEMENT
        f.writelines("\r\n")
        f.writelines(irrigation)
        # 
        # FERTILIZERS (INORGANIC)
        f.writelines("\r\n")
        f.writelines(fertilizers)
        # 
        # RESIDUES AND ORGANIC FERTILIZER
        #f.writelines("\r\n")
        #f.writelines(residues)
        # 
        # ENVIRONMENT MODIFICATIONS
        #f.writelines("\r\n")
        #f.writelines(environment)
        # 
        # HARVEST DETAILS - No needed 
        #f.writelines("\r\n")
        #f.writelines(harvest)
        # 
        # SIMULATION CONTROLS
        f.writelines("\r\n")
        f.writelines(simulation)
        # 
        # AUTOMATIC MANAGEMENT
        f.writelines("\r\n")
        f.writelines(automgnt)
        
    return True
        
#
def runDSSATSim_byCultivar_v2(df_tmp, INGENO=None, CNAME=None, WModel='CSCER', HDAP2AD=10, fldname='Calibrated',
                              byCultivar=False, allYrs=False, verbose=False):
    if (WModel!='CSCER'):
        print("Model not valid or not implemented yet")
        return
    sel_col = [ 'E','location', 'Occ', 'loc_code', 'country', 'locationname',  'Nursery', 'sowing',  'lat', 'lon']

    sel_col2 = ['E', 'location', 'Occ', 'loc_code', 'country', 'locationname',  'Nursery', 'sowing', 'lat', 'lon',
                'ObsYield', 'Days_To_Heading', 'Days_To_Anthesis', 'Days_To_Maturity', 
                'ObsHeadingDAP', 'ObsAnthesisDAP','ObsMaturityDAP']

    hoy = dt.datetime.now().strftime('%Y%m%d')
    loc_no_process = []
    df_summaries = pd.DataFrame()
    for E in tqdm(df_tmp['E'].unique()): #[:10]
        # Simulate Genotypes by location-occ-nursery
        fnWHX = None
        outdir = None
        FileX = False
        df_loc_occ_yr = df_tmp[sel_col2][df_tmp['E']==E].groupby(sel_col, as_index=False).agg('mean').reset_index(drop=True)
        try:
            loc_dssat_params = IWIN_params_DSSAT[IWIN_params_DSSAT['location']==df_loc_occ_yr.iloc[0]['location']]
            if (loc_dssat_params is not None or len(loc_dssat_params)>0):
                fnWHX = loc_dssat_params.iloc[0]['FileX']
                df_loc_occ_yr['INGENO'] = loc_dssat_params.iloc[0]['INGENOs'] if INGENO is None else INGENO
                df_loc_occ_yr['CNAME'] = loc_dssat_params.iloc[0]['CNAMEs'] if CNAME is None else CNAME
                df_loc_occ_yr['WSTA'] = loc_dssat_params.iloc[0]['FileX'] #'ERGP7940'
                df_loc_occ_yr['ID_SOIL'] = loc_dssat_params.iloc[0]['SOIL-HN27'] #'HN_GEN0016'
                #outdir =  f'/Users/ernestogiron/Desktop/AG2022/AI_IWIN/toDSSAT/results/{hoy}/DSSATv48/{fldname}/{WModel}/{E}'
                outdir =  os.path.join(RESULTS_IWIN_PATH,f'{hoy}/{fldname}/{WModel}/{E}')
                if not os.path.isdir(outdir):
                    os.makedirs(outdir, exist_ok=True)
                #output_file = outdir + '/{}.WHX'.format(loc_dssat_params.iloc[0]['FileX'])
                output_file = outdir + '/{}.WHX'.format(fnWHX)

                FileX = createWHX_simpleversion(df_loc_occ_yr, byCultivar, allYrs, output_file)
                #
                if ((FileX is True) and (outdir is not None)):
                    cwd = os.getcwd() # Esto a veces genera error cuando se elimimnan los outdir creados
                    os.chdir(outdir)
                    #print(outdir)
                    #!/usr/local/DSSAT48/dscsm048 CSCER048 A f'{fnWHX}.WHX'
                    if (WModel=='CSCER'):
                        cmd = f'/usr/local/DSSAT48/dscsm048 CSCER048 A {fnWHX}.WHX'
                    elif (WModel=='CSCRP'):
                        cmd = f'/usr/local/DSSAT48/dscsm048 CSCRP048 A {fnWHX}.WHX'
                    elif (WModel=='WHAPS'):
                        cmd = f'/usr/local/DSSAT48/dscsm048 WHAPS048 A {fnWHX}.WHX'
                    try:
                        completed_process = subprocess.run(cmd, shell=True,  
                                                           stdout=subprocess.PIPE, 
                                                           stderr=subprocess.STDOUT
                                                          )
                        if (completed_process.returncode < 0):
                            print("-"*80)
                            print('ERROR: Experimental file {}.WHX - {}'.format(fnWHX,E))
                            #print("-"*80)
                            print("Process was terminated by signal {} - {}"\
                                  .format(completed_process.returncode, completed_process.stderr))
                        else:
                            if (verbose is True):
                                print("Results:", completed_process.stdout.decode('utf-8'))
                            #if (retProcess is True):
                            #    return completed_process.stdout
                            #if (compress is True):
                            #    # Compress results
                            #    print('Zipping...')
                            # JOIN RESULTS
                            if (allYrs is False):
                                try:
                                    df_summary = pd.read_csv(os.path.join(outdir, 'summary.csv'), dtype={ "RUNNO": int, "HWAM": int,}, index_col=False)
                                    df_summary = df_summary.round({'HWUM': 4, 'H#UM': 1, 'HIAM': 3, 'HIAM':3, 'LAIX':1, 'N2OEC': 3,
                                                           'DMPPM': 1, 'DMPEM': 1, 'DMPTM': 1, 'DMPIM': 1, 'YPPM': 1, 'YPEM': 1, 'YPTM': 1, 
                                                           'YPIM': 1, 'DPNAM': 1, 'DPNUM': 1, 'YPNAM': 1, 'YPNUM': 1,
                                                           'TMAXA': 1, 'TMINA': 1, 'SRADA': 1, 'DAYLA': 1, 'CO2A': 1, 'PRCP': 1, 'ETCP': 1, 
                                                           'ESCP': 1, 'EPCP': 1
                                                          })
                                    sclmn = ['RUNNO', 'MODEL', 'TNAM', 'SOIL_ID', 'SDAT', 'PDAT', 'EDAT', 'ADAT',
                                             'MDAT', 'HDAT', 'HYEAR', 'DWAP', 'CWAM', 'HWAM', 'TMAXA', 'TMINA',
                                             'SRADA', 'DAYLA', 'CO2A', 'PRCP', 'ETCP'
                                            ]
    
                                    df_summary = pd.concat([df_loc_occ_yr, df_summary[sclmn]], axis=1)
                                    # Update 
                                    df_summary['SimYield'] = round(df_summary['HWAM'] / 1000, 3)
                                    #df_summary['ADAP'], df_summary['MDAP'] = zip(*df_summary.apply(getAnthesisMaturityDAP, axis=1 ))
                                    df_summary['ADAP'], df_summary['MDAP'], df_summary['HeadingDAP'] = zip(*df_summary.apply(getAnthesisMaturityDAPv2, axis=1 ))
                                    #df_summary['ADAP'], df_summary['MDAP'], df_summary['HeadingDAP'] = zip(*df_summary.apply(getAnthesisMaturityDAPv2(HDAP2AD), axis=1 ))
                                    df_summaries = pd.concat([df_summaries, df_summary], axis=0)
                                except Exception as err:
                                    if (verbose is True):
                                        print("Problem in {}, reading summary.csv. Error: {}".format(E, err))
                                    loc_no_process.append(E)
                                    pass
                        # Default params
                        os.chdir(cwd) #os.chdir(PROJECT_PATH+'code')
                    except subprocess.CalledProcessError as e:
                        if (verbose is True):
                            print("Error running DSSAT model. Error:",e.output)
                        # Default params
                        os.chdir(cwd) #os.chdir(PROJECT_PATH+'code')
                        pass
        except Exception as err:
            if (verbose is True):
                print("Error in location:{}. {}".format(E, err))
            loc_no_process.append(E)
            pass
    #
    return df_summaries, loc_no_process

#
def dispFigures_ObsVsSim_v2(df, isAvgByLocation=False, model='CERES', dirname = 'Comparison_Figures', fname='DSSAT_v48',
                            path_to_save_results='./',  saveFig=False, showFig=True, fmt='jpg'):
    df_uids_anthesis = df.copy()
    #fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, sharex=False, sharey=False,  figsize=(10,10))
    fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4,2, sharex=False, sharey=False,  figsize=(10,18))
    #fig.subplots_adjust(top=0.9)

    def createFigComp(dfsim, ax, fld1='ObsYield', fld2='SimYield', axisTitle='', s=40, lw=2, alpha=.95,
                      fc="none", clr="#ff6347", zorder=1, xscore_pos=0.05, yscore_pos=0.96, ha='left', va='top',
                      yld=True, dispScore=True):
        df = dfsim.copy()
        df.dropna(subset=[fld1, fld2], inplace=True)
        if (yld is True):
            hue='location'
            style='location'
            ec=None
            fc=fc
        else:
            hue=None
            style=None
            ec=clr
            fc=fc
        g = sns.scatterplot(x=fld1, y=fld2, data=df, hue=hue, style=style, #marker="$\circ$",
                            alpha=alpha, s=s, linewidth=lw, color=clr, zorder=zorder, fc=fc, edgecolor=ec,
                            ax=ax);
        #for dots in ax.collections:
        #    facecolors = dots.get_facecolors()
        #    dots.set_edgecolors(facecolors.copy())
        #    dots.set_facecolors('none')
        #    dots.set_linewidth(1)

        if (yld is True):
            g.set(xlim=(0, 14), ylim=(0, 14))
        else:
            g.set(xlim=(0, 300), ylim=(0, 300))
        #g.grid(b=True, which='major', color='#d3d3d3', linewidth=0.25)
        #g.grid(b=True, which='minor', color='#d3d3d3', linewidth=0.25)
        g.grid(which='major', color='#d3d3d3', linewidth=0.25)
        g.grid(which='minor', color='#d3d3d3', linewidth=0.25)
        ax.axline((0, 0), slope=1, c=".7", ls="--", lw=0.5, zorder=0)
        #ax.set_title('CROPSIM-CERES', fontsize=13)
        if (yld is True):
            ax.set_xlabel(f'Observed {axisTitle} (t ha$^{-1}$)', fontsize=10)
            ax.set_ylabel(f'Simulated {axisTitle} (t ha$^{-1}$)', fontsize=10)
        else:
            ax.set_xlabel(f'Observed {axisTitle} (DAP)', fontsize=10)
            ax.set_ylabel(f'Simulated {axisTitle} (DAP)', fontsize=10)
        if (yld is True):
            ax.get_legend().remove()
        #
        if (dispScore is True):
            r2score, rmse, n_rmse, d_index = getTraitScores(df, fld=fld1, fld2=fld2)
            clr2=clr if fld1=='ObsAnthesisDAP' or fld1=='ObsHeadingDAP' or fld1=='ObsMaturityDAP' else '#222'
            ax.text(xscore_pos, yscore_pos,'Observations:{}\nRMSE:{:.1f}\nn-RMSE:{:.1f}%\nd-index:{:.2f}\nR$^2$: {:.2f}'.format(len(df), rmse, n_rmse, d_index, r2score), 
                     fontsize=8, color=clr2, ha=ha, va=va, transform=ax.transAxes ) 

    df_uids_anthesis['location'] = df_uids_anthesis['location'].astype(str)
    if (len(df_uids_anthesis)>0):
        s=20
        s2=3
        # HEADING
        createFigComp(df_uids_anthesis, ax1, fld1='Days_To_Heading_old', fld2='HeadingDAP', axisTitle='Heading',
                      s=s, lw=1, alpha=.35, clr="brown", zorder=2, yld=False)
        createFigComp(df_uids_anthesis, ax1, fld1='ObsHeadingDAP', fld2='HeadingDAP', axisTitle='Heading',
                      s=s2, lw=1, alpha=.95, clr="red", zorder=1,
                      xscore_pos=0.96, yscore_pos=0.05, ha='right', va='bottom', yld=False)
        # Avg by Location
        if (isAvgByLocation is True):
            df_uids_anthesis_byLoc = df_uids_anthesis.groupby(['location'], as_index=False).agg('mean')
        else:
            df_uids_anthesis_byLoc = df_uids_anthesis.copy()
        # Use only select field 
        df_uids_anthesis_byLoc = df_uids_anthesis_byLoc[df_uids_anthesis_byLoc['Select']=='Keep']
        createFigComp(df_uids_anthesis_byLoc, ax2, fld1='Days_To_Heading_old', fld2='HeadingDAP', axisTitle='Heading',
                      s=s, lw=1, alpha=.35, clr="brown", zorder=2, yld=False)
        createFigComp(df_uids_anthesis_byLoc, ax2, fld1='ObsHeadingDAP', fld2='HeadingDAP', axisTitle='Heading',
                      s=s2, lw=1, alpha=.95, fc='#f00', clr="#f00", zorder=1,
                      xscore_pos=0.96, yscore_pos=0.05, ha='right', va='bottom', yld=False)
        #
        # ANTHESIS
        createFigComp(df_uids_anthesis, ax3, fld1='Days_To_Anthesis_old', fld2='ADAP', axisTitle='Anthesis',
                      s=s, lw=1, alpha=.35, clr="orange", zorder=2, yld=False)
        createFigComp(df_uids_anthesis, ax3, fld1='ObsAnthesisDAP', fld2='ADAP', axisTitle='Anthesis',
                      s=s2, lw=1, alpha=.95, clr="red", zorder=1,
                      xscore_pos=0.96, yscore_pos=0.05, ha='right', va='bottom', yld=False)
        # Avg by Location
        if (isAvgByLocation is True):
            df_uids_anthesis_byLoc = df_uids_anthesis.groupby(['location'], as_index=False).agg('mean')
        else:
            df_uids_anthesis_byLoc = df_uids_anthesis.copy()
        # Use only select field 
        df_uids_anthesis_byLoc = df_uids_anthesis_byLoc[df_uids_anthesis_byLoc['Select']=='Keep']
        createFigComp(df_uids_anthesis_byLoc, ax4, fld1='Days_To_Anthesis_old', fld2='ADAP', axisTitle='Anthesis',
                      s=s, lw=1, alpha=.35, clr="orange", zorder=2, yld=False)
        createFigComp(df_uids_anthesis_byLoc, ax4, fld1='ObsAnthesisDAP', fld2='ADAP', axisTitle='Anthesis',
                      s=s2, lw=1, alpha=.95, fc='#f00', clr="#f00", zorder=1,
                      xscore_pos=0.96, yscore_pos=0.05, ha='right', va='bottom', yld=False)
        #
        # MATURITY
        createFigComp(df_uids_anthesis, ax5, fld1='Days_To_Maturity_old', fld2='MDAP', axisTitle='Maturity',
                      s=s, lw=1, alpha=.95, clr="green", zorder=2, yld=False)
        createFigComp(df_uids_anthesis, ax5, fld1='ObsMaturityDAP', fld2='MDAP', axisTitle='Maturity',
                      s=s2, lw=1, alpha=.95, clr="red", zorder=1,
                      xscore_pos=0.96, yscore_pos=0.05, ha='right', va='bottom', yld=False)
        # Avg by Location
        if (isAvgByLocation is True):
            df_uids_anthesis_byLoc = df_uids_anthesis.groupby(['location'], as_index=False).agg('mean')
        else:
            df_uids_anthesis_byLoc = df_uids_anthesis.copy()
        # Use only select field 
        df_uids_anthesis_byLoc = df_uids_anthesis_byLoc[df_uids_anthesis_byLoc['Select']=='Keep']
        createFigComp(df_uids_anthesis_byLoc, ax6, fld1='Days_To_Maturity_old', fld2='MDAP', axisTitle='Maturity',
                      s=s, lw=1, alpha=.35, clr="green", zorder=2, yld=False)
        createFigComp(df_uids_anthesis_byLoc, ax6, fld1='ObsMaturityDAP', fld2='MDAP', axisTitle='Maturity',
                      s=s2, lw=1, alpha=.95, fc='#f00', clr="#f00", zorder=1,
                      xscore_pos=0.96, yscore_pos=0.05, ha='right', va='bottom', yld=False)
        
        # 
        # GRAIN YIELD
        createFigComp(df_uids_anthesis, ax7, fld1='ObsYield', fld2='SimYield', axisTitle='Yield', s=6, alpha=.95)
        # Avg by Location
        if (isAvgByLocation is True):
            df_uids_anthesis_byLoc = df_uids_anthesis.groupby(['location'], as_index=False).agg('mean')
        else:
            df_uids_anthesis_byLoc = df_uids_anthesis.copy()
        # Use only select field 
        df_uids_anthesis_byLoc = df_uids_anthesis_byLoc[df_uids_anthesis_byLoc['Select']=='Keep']
        createFigComp(df_uids_anthesis_byLoc, ax8, fld1='ObsYield', fld2='SimYield', axisTitle='Yield', s=6, alpha=.95)
        #
        # Save figure
        fig.tight_layout()
        # Save in PDF
        hoy = dt.datetime.now().strftime('%Y%m%d')
        figures_path = os.path.join(path_to_save_results, '{}_{}'.format(dirname, hoy))
        if not os.path.isdir(figures_path):
            os.makedirs(figures_path)
        if (saveFig is True and fmt=='pdf'):
            fig.savefig(os.path.join(figures_path,"{}_{}_{}.{}".format(model, fname, hoy, fmt)), 
                        bbox_inches='tight', orientation='portrait', #facecolor=fig.get_facecolor(),
                        edgecolor='none', transparent=False, pad_inches=0.5, dpi=300)
    
        if (saveFig==True and (fmt=='jpg' or fmt=='png')):
            fig.savefig(os.path.join(figures_path,"{}_{}_{}.{}".format(model, fname, hoy, fmt)), 
                        bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none', transparent=False, dpi=300)
    
        if (showFig is True):
            fig.show()
        else:
            del fig
            plt.close();





