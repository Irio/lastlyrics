import gdata.urlfetch
import gdata.service
import gdata.youtube
import gdata.youtube.service

def search(search_term):
  client = gdata.youtube.service.YouTubeService()
  query = gdata.youtube.service.YouTubeVideoQuery()
  query.vq = search_term
  query.max_results = '1'
  feed = client.YouTubeQuery(query)
  return {
    'title': feed.entry[0].title.text,
    'swf_url': feed.entry[0].GetSwfUrl(),
    'description': feed.entry[0].media.description
  } if feed.entry else None
