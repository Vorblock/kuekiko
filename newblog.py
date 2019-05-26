#coding:utf-8
import os,sys
##此脚本用于系统全局新建blog文章 使用newblog命令 只限自用

def newblog(blogname):
    env = os.environ
    BLOG_HOME = env.get('BLOG_HOME')
    blogsource = BLOG_HOME+"\\blog"
    print(os.getcwd())
    os.chdir(blogsource)
    print(os.getcwd())
    os.system(f'hugo new {blogname}')

if __name__ == "__main__":
    if len(sys.argv)== 2:
        print("新建文章："+ str(sys.argv[1])+".md")
        newblog('post/' + str(sys.argv[1]) +'.md')
    else:
        print("请输入创建的文章名")