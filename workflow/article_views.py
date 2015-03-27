from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from mainsite.models import Article, Issue,ArticleForm, Album
from workflow.models import WArticle, Revision
from workflow.views import group_required
from django.utils import timezone
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
import subprocess

class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/warticle.html"

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content', 'section','issue']
    template_name = 'articles/new_article.html'
    success_url = reverse_lazy('whome')

    def form_valid(self, form):
        article = form.save(commit=False)
        article.issue = Issue.objects.latest('created_date')
        article.save()
        article.authors.add(self.request.user.profile)
        album = Album(article=article)
        album.save()
        workflowArticle = WArticle(article=article, status='')
        workflowArticle.save()
        return super(ArticleCreateView, self).form_valid(form)

@group_required('silver')
def article_edit(request,issue_id,pk):
    original_article = Article.objects.get(pk=pk)
    original_content = original_article.content
    if request.method == 'GET':
        original_content = original_article.content
        original_second = original_article.updated_date.second
        form = ArticleForm(instance=original_article)
        return render(request,'articles/edit_article.html',
                      {'form':form,'original_content':original_content,'original_second':original_second})
    else:
        base_content = request.POST['original_content']
        base_second = request.POST['original_second']
        form = ArticleForm(request.POST, instance=original_article)
        if form.is_valid():
            if base_second == str(original_article.updated_date.second):
                article = form.save(commit=False)
                article.updated_date = timezone.now()
                article.save()
            else:
                article = form.save(commit=False)
                base = open('base','w');me = open('v1','w');other = open('v2','w')
                base.write(base_content)
                me.write(article.content)
                other.write(original_content)
                command=['bash','merge.sh']
                p = subprocess.Popen(command, stdout=subprocess.PIPE)
                text = p.stdout.read()
                print(text)
                article.content = text
                article.updated_date = timezone.now()
                article.save()
            revision = Revision(article=original_article,
                                    editor=request.user.profile, body=original_article.content)
            revision.save()
            return redirect(reverse('warticle',args=[issue_id,pk]))
        else:
            return render(request,'articles/edit_article.html',{'form':form})



class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "articles/article_confirm_delete.html"
    success_url = reverse_lazy('whome')