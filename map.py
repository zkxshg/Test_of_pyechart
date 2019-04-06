from pyecharts import Map
value = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
attr = ["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
map = Map("全国收入分布图", width=1200, height=600)
map.add(
    "年收入",
    attr,
    value,
    maptype="china",
    is_visualmap=True,
    visual_text_color="#000",
    is_label_show=True
)
map.render()