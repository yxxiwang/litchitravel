litchitravel
============

an app of share travel experence plantform

============20120701=========
初始化，定义数据结构，
Member 
    id = models.IntegerField()
    status = models.IntegerField(blank=True,default=0)
    regtime = models.DateTimeField('date published',blank=True)
    name = models.CharField(max_length=60,blank=True)
    password = models.CharField(max_length=200,blank=True)
    email = models.CharField(max_length=80,blank=True)
    following_count = models.IntegerField(blank=True,default=0)
    follows_count = models.IntegerField(blank=True,default=0)
    publish_count = models.IntegerField(blank=True,default=0)
    subscribe_count = models.IntegerField(blank=True,default=0)

Message 
    id = models.IntegerField()
    status = models.IntegerField(default=0)
    content = models.CharField(max_length=1000,blank=True)
    publish_uid = models.ForeignKey(Member)
    publish_time = models.DateTimeField('date published')