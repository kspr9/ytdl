from pytube import YouTube


def dl_video():

    url = str(input("Give video url: "))

    yt = YouTube(url)

    print("\n<-------------------  Video Title  ---------------------->\n")
    #get Video Title
    print(yt.title)

    print("\n<--------------  Display available streams  -------------->")
    print("""\nThese streams are video and audio in one. 
            For video only or audio only, modify stream filter in sourcecode""")
    # get all the stream resolution for the 
    #for stream in yt.streams:
    #    print(stream)

    for stream in yt.streams.filter(progressive=True):
        print(stream)

    print("\n<---------------  Stream selection  ---------------------->\n")
    # select preferred stream
    selected_stream = int(input("Which itag do you choose?: "))

    stream = yt.streams.get_by_itag(selected_stream)
    # Get highest resolution stream that is a progressive (video+audio) video.
    #stream = yt.streams.get_highest_resolution()
    print("\n<---------------  Download started  ---------------------->\nDownloading...")
    #Download video
    #my_video.download()
    stream.download()
    print("\n<----------------  Download finished  -------------------->\n")

if __name__ == "__main__":
    dl_video()
