# 接口  

## 参数调节

+ VP16的生成速度由主程序glusensor里面的framecount调节(每多少帧生成一个)  

+ 胞外glucose的生成目前也是通过framecount调节

+ insulin降解胞内glucose的范围(距离)和速率(lifespan减少速率)在CellSystem类里面的check()函数里面

+ insulin的生成数量取决于蛋白复合体在sensor上面黏附的时间(已转换为蛋白复合体的lifespan参数的减少速率)参数调节在CellSystem类里面的addInsulin()函数中

+ insulin在生成的时候就给了一定概率出胞(通过对其inCell参数的随机初始化实现)代码在ProteinSystem类中的addInsulin()函数中  

+ 细胞膜的颜色调节(通过小圆覆盖大圆的颜色留下来的边缘)在cell类中的display()函数调节fill()函数里面的参数，蓝光的颜色也是在这里调节  画板的背景色在draw()函数中的background()中调节

+ proteinSystem类中不同蛋白质的type属性分别是其名字的string

+ 各种粒子的个数调节也都可以通过其对应的生成函数即add%()函数中的for循环的循环次数调节

## 改进与未完成的工作

+ 胞外insulin的作用实现以及其与膜上insR受体结合启动负反馈调节途径(后续需加班)

+ 蛋白质生成过程中的mRNA过程实现(重点)

+ 各个sensor的形状大小设计以及glucose,Gal4,VP16,complex的形状大小设计

+ 加入杨成的设计工作 实现各个粒子有一定区分度

+ 定量工作(需要引入一些计数参数进来对一些速率进行调节)

+ 胞外环境还需设计(目前我还没有好想法)

+ 提议：为了让粒子之间不重叠可以加一个函数让它们之间存在一个较弱的互斥(有相关代码，我之前实现过一次效果一般，没有书上demo那种效果)

+ glucose的鼠标添加等后续工作完成之后应该调到胞外生成(因为吃东西的glucose都是吸收入血在胞外)当然这是小问题
