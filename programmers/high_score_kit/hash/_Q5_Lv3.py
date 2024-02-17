def solution(genres, plays):
    playtime_of_each_genre = {}
    playlist_of_each_genre = {}
    for i in range(len(genres)) :
        genre = genres[i]
        play = plays[i]
        if genre in playtime_of_each_genre.keys():
            playtime_of_each_genre[genre] += play
        else:
            playtime_of_each_genre[genre] = play

        if genre in playlist_of_each_genre.keys():
            playlist_of_each_genre[genre].append([play, i])
        else:
            playlist_of_each_genre[genre] = [[play, i]]

    for value in playlist_of_each_genre.values():
        value.sort(key=lambda x: (-x[0], x[1]))

    genre_list = list(playtime_of_each_genre.keys())
    genre_list.sort(key=lambda x: -playtime_of_each_genre[x])
    answer = []

    for genre in genre_list:
        count = 0
        for play in playlist_of_each_genre[genre]:
            if count == 2:
                break
            answer.append(play[1])
            count += 1


    return answer

# answer: [4, 1, 3, 0]
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
# answer: [1, 0]
print(solution(["classic", "pop"], [500, 600]))