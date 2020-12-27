from sanic import response
from sanic import Blueprint
from helpers.url_helper import UrlHelper
blueprint = Blueprint('my_blueprint')


@blueprint.route('/shorten', methods=['POST'])
def shorten_url(request):
    input_url = request.form['url']
    input_url = input_url[0]
    url_helper = UrlHelper()
    url = url_helper.insert(input_url)
    return response.json({'success': True, 'url': url.url, 'shortUrl': url.short_url, 'id': url.url_id})


@blueprint.route('/shorten/<short_url:string>', methods=['GET'])
def get_url(request, short_url):
    url_helper = UrlHelper()
    url = url_helper.get(short_url=short_url)
    if url is None:
        return response.json({'success': False, 'url': "url not found"}, status=404)
    return response.json({'success': True, "url": url.url})


@blueprint.route('/shorten/<url_id:int>', methods=['DELETE'])
def deleteShortUrl(request, url_id):
    url_helper = UrlHelper()
    url = url_helper.delete(url_id)
    if url is not None:
        return response.json({'success': True})
    else:
        return response.json({'success': False, 'url': "url not found"}, status=404)
