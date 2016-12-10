# encoding: UTF-8
import os
import json

categories = [u"床", u"桥", u"油", u"狗", u"猫", u"葱", u"锣", u"鹰", u"乌云", u"胶卷", u"人参", u"企鹅", u"光盘", u"兔子", u"公路", u"冰箱",
              u"刺猬", u"剪纸", u"南瓜", u"印章", u"卷尺", u"哑铃", u"啤酒", u"喷泉", u"围巾", u"土豆", u"墨镜", u"天线", u"天鹅", u"奖状", u"奶瓶",
              u"山楂", u"帐篷", u"干冰", u"年画", u"恐龙", u"戒指", u"手套", u"手机", u"扫把", u"扳手", u"报纸", u"披萨", u"拉链", u"数字", u"斑马",
              u"星星", u"月亮", u"本子", u"杏仁", u"枕头", u"树叶", u"核桃", u"梳子", u"椰子", u"楼梯", u"樱桃", u"毛巾", u"毛线", u"气球", u"水管",
              u"沙拉", u"沙漠", u"油条", u"洋葱", u"海滩", u"海豚", u"海豹", u"海鸥", u"游艇", u"漏斗", u"灯笼", u"烤鸭", u"熨斗", u"牙刷", u"牙膏",
              u"狮子", u"玛瑙", u"球拍", u"生姜", u"电线", u"白菜", u"皮球", u"盒子", u"盘子", u"砚台", u"磁铁", u"秋千", u"章鱼", u"竹席", u"算盘",
              u"箭头", u"箱子", u"篮球", u"粽子", u"红枣", u"红豆", u"红酒", u"纸牌", u"纽扣", u"经筒", u"绿豆", u"翅膀", u"翡翠", u"老虎", u"脸谱",
              u"舞狮", u"航母", u"芒果", u"花瓶", u"花生", u"花轿", u"茶几", u"药片", u"荷叶", u"菠萝", u"萝卜", u"蒸笼", u"薯条", u"蚂蚁", u"蚊子",
              u"蚊香", u"蛋挞", u"蜂蜜", u"蜗牛", u"蜜蜂", u"蜡烛", u"蜥蜴", u"蜻蜓", u"蝌蚪", u"蝴蝶", u"螃蟹", u"衣架", u"袋鼠", u"被子", u"裙子",
              u"西装", u"试管", u"话梅", u"贝壳", u"路灯", u"轮胎", u"钟表", u"钻石", u"铁轨", u"铁锹", u"铃铛", u"键盘", u"雕像", u"雨靴", u"青椒",
              u"青蛙", u"鞋刷", u"鞭炮", u"韭菜", u"风筝", u"飞机", u"饭盒", u"馄饨", u"骆驼", u"鱼缸", u"鱿鱼", u"鲨鱼", u"鸭蛋", u"龙舟", u"三明治",
              u"中国结", u"人民币", u"仙人球", u"仪表盘", u"传真机", u"保温杯", u"保龄球", u"创可贴", u"加湿器", u"发电机", u"喷雾器", u"图书馆", u"垃圾桶",
              u"塑料杯", u"塑料瓶", u"太阳能", u"安全帽", u"手掌印", u"手电筒", u"打字机", u"投影仪", u"报刊亭", u"排风机", u"摩天轮", u"收纳箱", u"收音机",
              u"文件夹", u"档案袋", u"榨汁机", u"油纸伞", u"游泳圈", u"游泳池", u"灭火器", u"热水器", u"热水瓶", u"热水袋", u"煤油灯", u"猫头鹰", u"电子秤",
              u"电热壶", u"电视机", u"电话亭", u"电话机", u"电饭煲", u"矿泉水", u"糖葫芦", u"紫砂壶", u"红绿灯", u"缝纫机", u"肥皂盒", u"自行车", u"苍蝇拍",
              u"蒙古包", u"西红柿", u"警示牌", u"订书机", u"调色板", u"辣椒酱", u"金字塔", u"钥匙圈", u"青花瓷", u"食用油", u"高压锅", u"七星瓢虫"]


def load_image_occurrence(path='/data2/heqingy/mapping.json'):
    assert os.path.isfile(path)

    with open(path) as f:
        _mappings = json.load(f)
    return _mappings['image_occurrence']


image_occurrence = load_image_occurrence()


writer10 = open('head_2000_occurence_10.txt', 'w')
writer7 = open('head_2000_occurence_7.txt', 'w')    
with open('head_2000.txt') as reader:
    for line in reader:
        rgb_key = eval(line.strip())[0]
        occurrence = image_occurrence[rgb_key]
	if occurrence >= 10:
		writer10.write(line.strip() + '\t' + str(occurrence) + '\n')
	elif occurrence >= 7:
		writer7.write(line.strip() + '\t' + str(occurrence) + '\n')

writer10.close()
writer7.close()        