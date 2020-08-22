from django import forms
from django.forms import Textarea

from .models import Post


class ContributionForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['topic', 'introduce','location']
        widgets = {
            'topic' : forms.TextInput(attrs={'placeholder':'比如: 大学物理实验'}),
            'location': Textarea(
                attrs={'cols': 50, 'rows': 5,
                       'placeholder':'比如: 网盘链接:xxxx 密码: xxxx'
                                     '\r(客官可留名也可不留名, '
                                     '若在此留名, 一定公开感谢!)'
                       }
            ),
            'introduce': forms.Textarea(
                attrs={'placeholder': '比如: 这个是最新的大学物理实验报告, 弥补了之前那份 xxx 部分的缺失, 而且字迹清晰',
                       'cols':50,
                       'rows':3,
                       }
            ),
        }
        labels = {
            'topic': ('科目'),
            'introduce':('简单介绍一下资源内容吧'),
            'location': ('留个链接给咱下载喽'),
        }
        help_texts = {
            'topic': ('   '),
            'introduce': ('   '),
            'location': ('   '),
        }
