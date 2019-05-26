#coding:utf-8
import os,sys
import time
##此脚本用于在我的Win10 上全局更新blog 
def autoupdate(str_argv):
    env = os.environ
    BLOG_HOME = env.get('BLOG_HOME')
    blogsource = BLOG_HOME+"\\blog"  ##博客源码所在目录
    blogdir = BLOG_HOME+"\\page"  ##博客git目录
    sdir = BLOG_HOME+"\\blog\\public"    ##博客源码生成的public目录 静态博客生成目录

    ##生成blog-git
    print(os.getcwd())  #打印当前目录
    os.chdir(blogsource) ##切换到博客源码所在目录
    print(os.getcwd())  ##打印切换的目录
    os.system('hugo')   ##执行命令生成静态blog源码

    ##执行命令git源码
    print(os.system('git add .'))
    print(os.system(f'git commit -m "{str_argv}"'))
    print(os.system('git push github dev'))
    print("github push完成!!!!")
    print(os.system('git push coding dev'))
    print("coding push完成!!!!")

    ## 复制blog
    print(sdir)
    print(blogdir)
    print(os.system("xcopy "+sdir+" "+ blogdir+" /E /Y"))

    ## git 静态blog
    print(os.getcwd())
    os.chdir(blogdir)  ## 切换目录
    print(os.getcwd())   
    print(os.system('git add .'))
    print(os.system(f'git commit -m "{str_argv}"'))
    print(os.system('git push github master'))
    print("github更新完成!!!!")
    print(os.system('git push coding master'))
    print("coding更新完成!!!!")


if __name__ ==  "__main__":
    if len(sys.argv)==2:  ##参数1:git的备注
        print(str(sys.argv[1]))
        autoupdate(str(sys.argv[1]))
    else:
        str_argv = '默认更新'+time.ctime() #不加任何命令的情况下
        autoupdate(str_argv)
