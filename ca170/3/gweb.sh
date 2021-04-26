# when testing, comment/uncomment the following "exec" line
# comment - output goes to screen
# uncomment - output goes to file

exec > gweb.output.html

d="/shared/humphrys/shakespeare"

cd $d

clickable()
{
 while read line
 do
  file=`echo "$line" | cut -f1 -d':'`
  hit=`echo "$line" | cut -f2- -d':'`
  echo "<a href='$d/$file'>$file</a>: $hit <br>"
 done
}
echo '<pre>'
grep -i "$1"  */*html | sed -e 's|<|\&lt;|g' | sed -e 's|>|\&gt;|g' | clickable
echo '</pre>'
