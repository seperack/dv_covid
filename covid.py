import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.ticker as tkr

#Goal is to plot an informational chart of COVID-19 data
#source: https://covidtracking.com/data/download/national-history.csv
#'https://stackoverflow.com/questions/44825950/matplotlib-create-two-subplots-in-line-with-two-y-axes-each'
#How to plot multiple subplots with shared y axis
#'https://www.youtube.com/watch?v=GeZVxiZqT4E'
#How to add a thousand comma separator 
#https://www.kite.com/python/answers/how-to-label-matplotlib-data-points-in-python
#Adding annotation

file = 'https://covidtracking.com/data/download/national-history.csv'
df = pd.read_csv(file, parse_dates=True, index_col='date')
print(df.columns)

def yfunc(y,pos):
    s='{:0,d}'.format(int(y))
    return s

def label(y):
    s='{:0,d}'.format(int(y))
    return s


y_format = tkr.FuncFormatter(yfunc)

def get_plot(ax1,x,y1,y2, y1_label, y2_label, c1,c2):
    """Input data to make subplot"""
    ax2 = ax1.twinx()
    ax1.yaxis.set_major_formatter(y_format)
    ax1.annotate(label(y1[0]), xy=(x[0], y1[0]), xytext=(x[150], y1[20]), arrowprops={"arrowstyle": "->", "color": c1})
    ax2.annotate(label(y2[0]), xy=(x[0], y2[0]), xytext=(x[50], y2[-1]), arrowprops={"arrowstyle": "->", "color": c2})
    ax2.yaxis.set_major_formatter(y_format)
    ax1.plot(x,y1,color=c1)
    ax2.plot(x,y2,color=c2)
    ax1.set_ylabel(y1_label, color=c1)
    ax2.set_ylabel(y2_label, color=c2)

#Syntax on how to format plot
#fig, (ax1, ax2) = plt.subplots(2,1)
#ax1, ax1a = get_plot(ax1,x,y1,y2, y1_label, y2_label, c1,c2)
#ax2, ax2a = get_plot(ax2,x,y1,y2, y1_label, y2_label, c1,c2)

fig, (ax1, ax2) = plt.subplots(2,1, sharex=True, figsize = (10,8))
get_plot(ax1,df.index,df['positive'], df['positiveIncrease'], 'Total positive', 'Daily positive tests', 'r', 'b')
get_plot(ax2,df.index,df['death'], df['deathIncrease'], 'Total deaths', 'Daily deaths', 'r', 'b')
ax1.set_title('COVID-19 Data in USA')
plt.show()








