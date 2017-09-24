from lino.api import dd

@dd.python_2_unicode_compatible
class Tag(dd.Model):
  
    name = dd.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
