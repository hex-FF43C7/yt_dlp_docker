# yt_dlp_docker

a docker container set up to automatically run yt-dlp

format for catalog:

[url]
[url] (B, E)
[url] (B, 4:47)
[url] (2:38, E)
[url] (30, 7:30)

parenthasys define start of clip and end of clip. Hashtags coment lines

enter in teminal to run while cwd is yt_dlp_docker:
***docker compose down; docker compose build; docker compose up***

run and bash into container:
docker compose down; docker compose build; docker compose up -d; docker exec -it yt_dlp_c bash
