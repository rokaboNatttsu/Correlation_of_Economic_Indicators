# オブジェクトの定義

### plotter = Plotter()


# メソッド

### plotter.set_data()

ｘ軸とｙ軸の変数を選ぶ



### plotter.range_scatter(xrange=[x下限, x上限], yrange=[y下限, y上限])
散布図のプロット。

xrangeでx方向のプロット範囲を指定。

yrangeでy方向のプロット範囲を指定。

引数のxrange,yrangeは省略可能。省略した場合、対象となるデータをすべてプロット。



### plotter.range_hist2d(xrange=[x下限, x上限], yrange=[y下限, y上限], xybins=[x方向の分割数,y方向の分割数], logscale=True)

二次元ヒストグラムのプロット。

xrangeでx方向のプロット範囲を指定

yrangeでy方向のプロット範囲を指定

引数のxrange,yrangeは省略可能。省略した場合、対象となるデータをすべてプロット。

xybinsでx方向とy方向の分割数の指定。デフォルトは100づつ。

logscale=Trueのとき、二次元ヒストグラムはlogスケールでプロット。
logscale=Falseのとき、二次元ヒストグラムは線形スケールでプロット。
logscaleは省略可能で、省略した場合、logスケールでプロットされる。
