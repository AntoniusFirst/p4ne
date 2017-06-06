from matplotlib import pyplot
from openpyxl import load_workbook

def getvalue(x): return x.value

wb=load_workbook('data_analysis_lab.xlsx')

sheet=wb['Data']
a=list(map(getvalue, sheet['A'][1:]))
b=list(map(getvalue, sheet['B'][1:]))
c=list(map(getvalue, sheet['C'][1:]))

pyplot.plot(a, b)
pyplot.plot(a, c)
pyplot.show()


