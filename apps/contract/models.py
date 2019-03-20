from django.db import models

# Create your models here.

class ContractsCategory(models.Model):
    '''
    合同分类
    '''
    CATEGORY_TYPE = {
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    }

    name = models.CharField('类别名',default="", max_length=30,help_text="类别名")
    code = models.CharField("类别code",default="", max_length=30,help_text="类别code")
    desc = models.TextField("类别描述",default="",help_text="类别描述")
    #目录树级别
    category_type = models.IntegerField("类目级别",choices=CATEGORY_TYPE,help_text="类目级别")
    # 设置models有一个指向自己的外键
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_cat")
    is_tab = models.BooleanField("是否导航",default=False,help_text="是否导航")
    add_time = models.DateTimeField("添加时间",default=datetime.now)

    class Meta:
        verbose_name = "合同类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 合同对象
class Contract(models.Model):
    name = models.CharField(max_length=150, unique=True)
    id = models.IntegerField(primary_key=True)
    number = models.CharField(max_length=150)
    hash_number = models.CharField(max_length=150)
    opinion = models.TextField()
    money = models.FloatField()
    type = models.CharField(max_length=150)
    summary = models.CharField(max_length=150)
    dept = models.CharField(max_length=150)
    verify = models.BooleanField()
    responsible_person = models.CharField(max_length=150)
    supplier_id = models.IntegerField()
    status = models.IntegerField()

# 电子合同存放地址表
class Contract_Location(models.Model):
    id = models.IntegerField(primary_key=True)
    contract_id = models.IntegerField()
    location = models.FilePathField()
    create_time = models.DateTimeField()
    create_by = models.CharField(max_length=150)
    status = models.IntegerField()

# 扫描件信息表
class Scan_Info(models.Model):
    id = models.IntegerField(primary_key=True)
    contract_id = models.IntegerField()
    name = models.CharField(max_length=150)
    location = models.FilePathField()
    status = models.IntegerField()
    verify_result = models.IntegerField()
    review_result = models.IntegerField()
    review_by = models.CharField(max_length=150)
    create_time = models.DateTimeField()
    create_by = models.CharField(max_length=150)
    update_time = models.DateTimeField()
    update_by = models.CharField(max_length=150)
    review_remark = models.TextField()

# 供应商表
class Supplier(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    manager = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)
    remark = models.TextField()

# 菜单表
class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    create_time = models.DateTimeField()
    create_by = models.CharField(max_length=150)
    update_time = models.DateTimeField()
    update_by = models.CharField(max_length=150)
    parent_id = models.IntegerField()
    name = models.CharField(max_length=150)
    icon = models.ImageField()
    url = models.URLField()
    server_url = models.URLField()
    type = models.CharField(max_length=150)
    tips = models.TextField()
    status = models.IntegerField()

#合同操作记录
class Contract_Oprea(models.Model):
    id = models.IntegerField(primary_key=True)
    contract_id = models.IntegerField()
    scan_id = models.IntegerField()
    opera_type = models.IntegerField()
    opera_by = models.CharField(max_length=150)
    opera_time = models.DateTimeField(auto_now_add=True) #auto_now无论是你添加还是修改对象，时间为你添加或者修改的时间。auto_now_add为添加时的时间，更新对象时不会有变动
