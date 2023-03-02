# define the function to calculate the optimal page replacement
def optimal_page_replacement(pages, frames):
    # initialize the list of frames and the number of page faults
    page_faults = 0
    frame_list = []
    
    # iterate through each page in the list of pages
    for page in pages:
        # if the page is not in the frame list, we have a page fault
        if page not in frame_list:
            # if there is still space in the frames, add the page to the frame list
            if len(frame_list) < frames:
                frame_list.append(page)
            # if there is no space in the frames, find the page that will not be used for the longest time in the future
            else:
                future = []
                # iterate through each page in the frame list
                for f in frame_list:
                    # find the index of the next occurrence of the page in the list of pages
                    try:
                        index = pages.index(f, pages.index(page))
                    except ValueError:
                        index = len(pages)
                    # append the index to the future list
                    future.append(index)
                # find the page with the maximum index (i.e. the page that will not be used for the longest time in the future)
                max_index = future.index(max(future))
                # replace the page with the maximum index with the current page
                frame_list[max_index] = page
            # increment the number of page faults
            page_faults += 1
    
    # return the number of page faults
    return page_faults
pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
frames = 3

page_faults = optimal_page_replacement(pages, frames)

print("Number of page faults:", page_faults)

