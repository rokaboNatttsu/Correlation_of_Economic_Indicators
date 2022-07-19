import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from copy import deepcopy
import seaborn as sns
import os
from matplotlib.colors import LogNorm

class Plotter:
    def __init__(self):
        self.x_variable = None
        self.y_variable = None
        self.x_data_name = None
        self.y_data_name = None

    def search_data_name(self):
        path = "data/calculated/SingleYear/"
        print("0, 国単位の変数")
        print("1, 一人当たりの変数")
        if input("数字を選択して入力:") == "0":
            path += "per_nation/"
        else:
            path += "per_person/"
        print()
        print("1, 成長率")
        print("2, 現地通貨建ての変数")
        print("3, GDP比")
        print("4, GDP比の増加幅")
        print("5, 人口")
        n = input("数字を選択して入力:")
        if n == "1":
            path += "growth_rate/"
        elif n == "2":
            path += "national_currency_variables/"
        elif n == "3":
            path += "per_GDP/"
        elif n == "4":
            path += "diff_rate/"
        else:
            path += "national_currency_variables/人口.csv"
            db = pd.read_csv(path)
            return db, "人口"
        
        files = os.listdir(path)
        for i, file_name in enumerate(files):
            value_name, _ = file_name.split(".")
            print(i+1, ", " + value_name)
        n = int(input("数字を選んで選択:"))
        path += files[n-1]
        db = pd.read_csv(path)
        choosed_data_name, _ = files[n-1].split(".")
        return db, choosed_data_name

    def choose_data(self):
        print("x軸の変数を選ぶ")
        x_variable, x_data_name = self.search_data_name()
        print()
        print("y軸の変数を選ぶ")
        y_variable, y_data_name = self.search_data_name()
        self.x_variable = x_variable
        self.y_variable = y_variable
        self.x_data_name = x_data_name
        self.y_data_name = y_data_name

    def drop_unfilled_countries(self):
        countries_lst = list(set(self.x_variable["Country"]) & set(self.y_variable["Country"]))
        M = min(len(list(self.x_variable.columns)), len(list(self.y_variable.columns)))
        col = ["Country"] + list(self.x_variable.columns)[-M+1:]
        new_x_variable = pd.DataFrame(np.zeros((len(countries_lst), M)), columns=col)
        new_y_variable = pd.DataFrame(np.zeros((len(countries_lst), M)), columns=col)
        new_x_variable["Country"] = countries_lst
        new_y_variable["Country"] = countries_lst
        for i, country in enumerate(countries_lst):
            t = list(self.x_variable[self.x_variable["Country"]==country].values[0])
            new_x_variable.iloc[i,1:] = t[1:]
            t = list(self.x_variable[self.x_variable["Country"]==country].values[0])
            new_y_variable.iloc[i,1:] = t[1:]

        self.x_variable = new_x_variable
        self.y_variable = new_y_variable

    def set_data(self):
        self.choose_data()
        self.drop_unfilled_countries()


    def range_scatter(self, xrange=[None, None], yrange=[None, None]):
        x_arr = np.array(self.x_variable.values[:][1:])
        y_arr = np.array(self.y_variable.values[:][1:])

        country_lst = list(self.x_variable["Country"])
        country_lst.sort()
        print("対象となった国の一覧")
        for country in country_lst:
            print(country)
        print("******************")

        x_1d, y_1d = x_arr.reshape(len(x_arr)*len(x_arr[0,:])), y_arr.reshape(len(y_arr)*len(y_arr[0,:]))
        #print("R =",np.corrcoef(x_1d, y_1d)[0,1])
        #print("R^2 =", np.corrcoef(x_1d, y_1d)[0,1]**2)

        m = max(np.min(x_1d), np.min(y_1d))
        M = min(np.max(x_1d), np.max(y_1d))

        plt.plot([m,M], [m,M], color = 'orange', linewidth=0.5)
        plt.scatter(x_1d, y_1d)
        plt.xlabel(self.x_data_name + " (%)", fontname="MS Gothic")
        plt.ylabel(self.y_data_name + " (%)", fontname="MS Gothic")
        plt.grid("both")
        plt.xlim(xrange)
        plt.ylim(yrange)
        plt.show()

    def range_hist2d(self, xrange=[None, None], yrange=[None, None], xybins=[100,100], logscale=True):
        x_arr = np.array([self.x_variable.values[i][1:] for i in range(len(self.x_variable.values))])
        y_arr = np.array([self.y_variable.values[i][1:] for i in range(len(self.y_variable.values))])
        
        country_lst = list(self.x_variable["Country"])
        country_lst.sort()
        print("対象となった国の一覧")
        for country in country_lst:
            print(country)
        print("******************")

        x_1d, y_1d = x_arr.reshape(len(x_arr[:,0])*len(x_arr[0,:])), y_arr.reshape(len(y_arr[:,0])*len(y_arr[0,:]))
        #print(np.sum(x_1d))
        #R = np.corrcoef(x_1d, y_1d)[0,1]
        #print("R =", R)
        #print("R^2 =", R**2)
        
        if logscale:
            plt.hist2d(x_1d, y_1d, bins=xybins, norm=LogNorm())
        else:
            plt.hist2d(x_1d, y_1d, bins=xybins)
        plt.xlabel(self.x_data_name + " (%)", fontname="MS Gothic")
        plt.ylabel(self.y_data_name + " (%)", fontname="MS Gothic")
        plt.grid("both")
        plt.colorbar()
        plt.xlim(xrange)
        plt.ylim(yrange)
        plt.show()


plotter = Plotter()
plotter.set_data()

plotter.range_hist2d()