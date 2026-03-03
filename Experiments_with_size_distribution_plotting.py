# Code to plot atmospheric aerosol data from a book we found 
# Need reference here
import pandas        #  For reading and parcing the csv file
import pathlib       #  For finding the silly file on Windows
import numpy as np
import matplotlib.pyplot as plt

# import histogram concentration data with lower and upper bin limits
file_to_open = pathlib.Path(r'C:\Users\rtlines\OneDrive - BYU-Idaho\BYUI-Synced\Non Class Material\Research\Scattering\SizeDistribution\Aerosol_data.csv')
print("file opened",file_to_open)
df = pandas.read_csv(file_to_open)   # read the file into a data frame
# Print out the data frame just to be sure we got the right data
print("file name", file_to_open)
print(df.keys)
print("\n")
# The data is structured as a column of names and a second column of emails
cnt = df.shape[0]      # get the number of rows of email addresses
print("there are ")
print(cnt)             # and print it for good measure
print("data pionts \n")
print(df.columns)     # prints a list of coumns in the spreadsheet
lbin=df['Lower_Size_Range(um)']
ubin=df['Upper_Size_range(um)']
conc=df['Concentration(cm**-3)']
print(lbin)
print(ubin)
print(conc)


# We want a fancy histogram where the bar size changes
w=ubin-lbin  # width of each bar
xticks=[]    # place where the bar centers go
# calculate the bar centers
for n, c in enumerate(w):
    xticks.append(sum(w[:n]) + w[n]/2)

plt.subplot(3, 2, 1)
plt.bar(xticks, height = conc, width = w, alpha = 0.8)
plt.subplot(3, 2, 2)
plt.bar(xticks[0:5], height = conc[0:5], width = w[0:5], alpha = 0.8)


# now normalize by size range
nconc=conc/w
plt.subplot(3, 2, 3)
plt.bar(xticks, height = nconc, width = w, alpha = 0.8)
plt.subplot(3, 2, 4)
plt.bar(xticks[0:5], height = nconc[0:5], width = w[0:5], alpha = 0.8)
# now let's make it a log scale in concentration
llbin=np.log(lbin)
lubin=np.log(ubin)
lw=lubin-llbin
lxticks=[]    # place where the bar centers go
# calculate the bar centers
for n, c in enumerate(w):
    lxticks.append(sum(lw[:n]) + lw[n]/2)
plt.subplot(3, 2, 5)
plt.bar(lxticks, height = nconc, width = lw, alpha = 0.8)
plt.subplot(3, 2, 6)
plt.bar(lxticks[0:5], height = nconc[0:5], width = lw[0:5], alpha = 0.7)


plt.show
