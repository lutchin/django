/**
 * Created by pavel on 10.7.17.
 */
var items=1;
function AddItem() {
  div=document.getElementById("items");
  button=document.getElementById("add");
  items++;
  newitem="<strong>Name " + items + ": </strong>";
  newitem+="<input type=\"text\" name=\"" + items;
  newitem+="\" size=\"20\"";
  newitem+="><br>";
  newnode=document.createElement("span");
  newnode.innerHTML=newitem;
  div.insertBefore(newnode,button);
}