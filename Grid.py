from pyecharts import Line, Page,Gauge
line = Line("本周气温")
attr = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
line.add(
    "最高气温",
    attr,
    [11, 11, 15, 13, 12, 13, 10],
    mark_point=["max", "min"],
    mark_line=["average"],
)
line.add(
    "最低气温",
    attr,
    [1, -2, 2, 5, 3, 2, 0],
    mark_point=["max", "min"],
    mark_line=["average"],
    legend_pos="20%",
)
gauge = Gauge("湿度计量表")
gauge.add(
    "最佳湿度",
    "实际湿度",
    66.66,
    angle_range=[180, 0],
    scale_range=[0, 100],
    is_legend_show=True,
)
page = Page()
page.add(line)
page.add(gauge)
page.render()
