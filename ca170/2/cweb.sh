if test "$2" = ""
then
 echo "Error. Not enough arguments."
 exit
fi

# Read in the arguments:

OLDSTRING=$1
NEWSTRING=$2

shift
shift

for file in $*
do
  ls -l $file 
  cat $file | sed -e "s|$OLDSTRING|$NEWSTRING|g" > tmpfile
  mv tmpfile $file
  echo
done