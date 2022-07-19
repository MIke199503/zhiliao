from pyecharts.charts import Bar
from pyecharts.charts import Line
from pyecharts.globals import ThemeType
import pyecharts.options as opts
from pyecharts.charts import Page
import pandas as pd


df1 = pd.read_excel('./区域销售及目标对比.xlsx')
df2 = pd.read_excel('./年度财务月度收支数据.xlsx')
df3 = pd.read_excel('./月度支出成本数据.xlsx')
df4 = pd.read_excel('./月度经营数据.xlsx')
c = (
    Line({"theme": ThemeType.MACARONS})
    .add_xaxis(df4['日期'].values.tolist())
    .add_yaxis("收入", df4['收入'].values.tolist())
    .add_yaxis("成本", df4['成本'].values.tolist())
    .add_yaxis("费用", df4['费用'].values.tolist())
    .add_yaxis("利润", df4['利润'].values.tolist())
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False), linestyle_opts=opts.LineStyleOpts(width=3))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="月度经营数据分析表", subtitle="2020年8月", pos_left= "center",
                                 title_textstyle_opts=opts.TextStyleOpts(font_size=30)),
        datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        legend_opts=opts.LegendOpts(pos_left="right", pos_top='center', orient='vertical')
    )

)
c1 = (
    Bar()
    .add_xaxis(df2['月份'].values.tolist())
    .add_yaxis("收入", df2['收入'].values.tolist())
    .add_yaxis("支出", df2['支出'].values.tolist())
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False), linestyle_opts=opts.LineStyleOpts(width=3))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="月度收支报表", subtitle="2020年", pos_left= "center",
                                 title_textstyle_opts=opts.TextStyleOpts(font_size=30)),
        datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        legend_opts=opts.LegendOpts(pos_left="right", pos_top='center', orient='vertical')
    )

)
l1 = df2['支出'].values.tolist()
l2 = df2['月份'].values.tolist()
from pyecharts import options as opts
from pyecharts.charts import Pie


p = (
    Pie()
    .add(
        "月份",
        [list(z) for z in zip(l2, l1)],
        radius=["40%", "60%"],
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            background_color="#eee",
            border_color="#aaa",
            border_width=1,
            border_radius=4,
                        rich={
                "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                "abg": {
                    "backgroundColor": "#e3e3e3",
                    "width": "100%",
                    "align": "right",
                    "height": 22,
                    "borderRadius": [4, 4, 0, 0],
                },
                "hr": {
                    "borderColor": "#aaa",
                    "width": "100%",
                    "borderWidth": 0.5,
                    "height": 0,
                },
                "b": {"fontSize": 16, "lineHeight": 33},
                "per": {
                    "color": "#eee",
                    "backgroundColor": "#334455",
                    "padding": [2, 4],
                    "borderRadius": 2,
                },
            },
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="每月支出占比", subtitle='2020年', pos_left='center',
                                              title_textstyle_opts=opts.TextStyleOpts(font_size=30)),
    legend_opts=opts.LegendOpts(pos_left="right", pos_top='center', orient='vertical')
                    )
)
l3 = df3['支出类目'].values.tolist()
l4 = df3['金额（万元）'].values.tolist()
p1 = (
        Pie()
        .add(
            series_name="访问来源",
            data_pair=[list(z) for z in zip(l3, l4)],
            rosetype="radius",
            radius="55%",
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="各项成本占比",
                subtitle='2020年',
                pos_left="center",
                pos_top="20",
                title_textstyle_opts=opts.TextStyleOpts(font_size=30),
            ),
            legend_opts=opts.LegendOpts(pos_left="right", pos_top='center', orient='vertical'),
        )
        .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
            label_opts=opts.LabelOpts(color="rgba(0, 0, 0, 0.3)"),
        )
    )
page = (
    Page(layout=Page.SimplePageLayout)
    .add(c)
    .add(c1)
    .add(p)
    .add(p1)

)
page.render('可视化展示.html')