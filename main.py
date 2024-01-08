from memes.GetSourceFile import GetSourceFile
from memes.makeTitleYoutube import MakeYoutubeTitle

text = "Juan"

M = GetSourceFile(text,9);
M.search_imag()

g = MakeYoutubeTitle()
g.make_text_title_and_views(text,g.human_format(),g.time_ago())
g.merges_tamplate_image()