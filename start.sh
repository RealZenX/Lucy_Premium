#Dont change anything without informing us
if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/RealZenX/Lucy_Premium.git /Lucy_Premium
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Lucy_Premium
fi
cd /Lucy_Premium
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
