server {
        server_name back.monogatari-guide.com;

        location / {
                proxy_pass http://0.0.0.0:8000;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
        }
        location /django_static/ {
                alias /home/backend_monogatari_guide/static/;
    }
        location /media/ {
                alias /home/backend_monogatari_guide/media/;
    }

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/back.monogatari-guide.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/back.monogatari-guide.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot


}
server {
    if ($host = back.monogatari-guide.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


        listen 80;
        server_name back.monogatari-guide.com;
    return 404; # managed by Certbot
}
