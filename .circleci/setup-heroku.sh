 #!/bin/bash
wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh

cat > ~/.netrc << EOF
machine api.heroku.com
  login $HEROKU_LOGIN
  password $HEROKU_API_KEY
EOF

cat >> ~/.ssh/config << EOF
  VerifyHostKeyDNS yes
  StrictHostKeyChecking no
EOF
