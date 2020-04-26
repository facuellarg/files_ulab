
for  file in ./data/; do
    # echo "$author_information"
    mongoimport --db VT --collection "$file" --file "$file" --type json --jsonArray
done;