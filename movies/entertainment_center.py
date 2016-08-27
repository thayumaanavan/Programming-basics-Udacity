import media


toy_story=media.Movie("Toy Story",
"A story of toy",
"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
"https://www.youtube.com/watch?v=KYz2wyBy3kc")



avatar=media.Movie("Avatar",
"science fiction",
"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
"https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwivoono3eDOAhUjTo8KHfYYCZUQyCkIHTAA&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DcRdxXPV9GNQ&usg=AFQjCNHfVhtBllyBLFd0YxZtVNRkrKF6gQ&sig2=YryQ--RG_ik3ao8EJ5tA2g&bvm=bv.131286987,d.c2I")


#avatar.show_trailer()
import fresh_tomatoes
movies=[toy_story,avatar]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)