# Define a corpus of web pages
corpus = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}

# Set the damping factor
damping_factor = 0.85
def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    N=len(corpus.keys())
    PageRank={page:1/N for page in corpus}
    outlink_count={page:len(outlinks) for page,outlinks in corpus.items()}

    while True:
        new_pagerank={}
        for page in corpus:
            incoming_pagerank=sum(PageRank[link]/outlink_count[link] for link in corpus if page in corpus[link])
            new_pagerank[page]=(((1-damping_factor)/N)+damping_factor*incoming_pagerank)
        if (sum(new_pagerank[page])==1 for page in corpus):
            break
        PageRank=new_pagerank
    total_pagerank=sum(PageRank.values())
    PageRank={page: rank/total_pagerank for page, rank in PageRank.items()}
    return PageRank

# Calculate the PageRanks using the iterate_pagerank function
pagerank = iterate_pagerank(corpus, damping_factor)

# Sum the PageRank values
total_pagerank =pagerank

# Print the result
print(total_pagerank)
