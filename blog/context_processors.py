from django.contrib.sites.models import Site
from django.db.models import Count
from .forms import PostSerachForm
from .models import (
    Category, Tag, Link, Analytics, Ads, SiteDetail, Comment,
    PopularPost,
)


def common(request):
    """どのテンプレートにも渡すデータの作成"""
    # サイト詳細情報の取得、もしくは作成
    try:
        mysite = SiteDetail.objects.latest('pk')
    except SiteDetail.DoesNotExist:
        # pk=1のSiteは必ずある。settings.pyで設定済み
        mysite = SiteDetail.objects.create(site=Site.objects.get(pk=1))

    context = {
        # カテゴリを紐付いた記事数順に取得。category.num_postsで件数が取得可
        'categories': Category.objects.annotate(
            num_posts=Count('post')).order_by('-num_posts'),
        # タグを紐付いた記事数順に取得。tag.num_postsで件数が取得可
        'tags': Tag.objects.annotate(
            num_posts=Count('post')).order_by('-num_posts')[:10],
        # コメントを返信コメント数順に取得。comment.num_recommentsで件数が取得可
        'comments': Comment.objects.annotate(
            num_recomments=Count('recomment')).order_by('-created_at')[:10],

        'links': Link.objects.all(),  # 全てのリンク
        'analytics': Analytics.objects.all(),  # アナリティクス
        'ads': Ads.objects.all(),  # 全ての広告
        'global_form': PostSerachForm(request.GET),  # 上部の検索フォーム
        'mysite': mysite,  # サイト詳細情報
        'popular_post_list': PopularPost.objects.order_by('-page_view'),  # 人気記事
    }
    return context
