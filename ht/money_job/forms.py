from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['subject', 'how_much', 'job_detail','deadline','contact','post_date']
        widgets = {
            'job_detail':forms.Textarea(
                attrs={'cols':40,
                       'rows':5,
                       'placeholder':"比如: xxx 报告, xxx 学期, xxx 实验部分",
                       }
            ),
            'subject':forms.TextInput(
                attrs={
                    'placeholder':"比如: 大学物理实验报告",
                }
            ),
            'deadline': forms.Textarea(
                attrs={
                    'placeholder': "比如: 2020年10月5日下午一节课以前",
                    'cols': 40,
                    'rows': 5,
                }
            ),
            'deadline': forms.Textarea(
                attrs={
                    'placeholder': "比如: 2020年10月5日下午一节课以前",
                    'cols': 40,
                    'rows': 5,
                }
            ),
            'contact': forms.Textarea(
                attrs={
                    'placeholder': "比如: 邮箱12345678@xxx.com",
                    'cols': 40,
                    'rows': 2,
                }
            ),

        }
        labels = {
            'subject':'科目',
            'how_much': '悬赏金额(单位:元)',
            'job_detail': '任务细节',
            'deadline': '截止日期',
            'contact': '联系方式',
            'post_date': '发布时间(自动填写)',
        }
        help_texts = {
            'subject': ('   '),
            'how_much': ('   '),
            'job_detail': ('   '),
            'deadline': ('   '),
            'contact': ('   '),
            'post_date': ('   '),
        }
