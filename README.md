# yt_dlp_docker

a docker container set up to automatically run yt-dlp

format for catalog:

[url]<br>
[url] (B, E)<br>
[url] (B, 00:04:47)<br>
[url] (00:02:38, E)<br>
[url] (30, 00:07:30)<br>

(hh:mm:ss)

parenthasys define start of clip and end of clip. Hashtags coment lines

enter in teminal to run while cwd is yt_dlp_docker:<br>
***docker compose down; docker compose build; docker compose up***

run and bash into container:<br>
docker compose down; docker compose build; docker compose up -d; docker exec -it yt_dlp_c bash
