#jupyter notebook --NotebookApp.token=test-secret --NotebookApp.allow_origin='http://127.0.0.1:8888' &

# remove jupyter_execute folder
for filename in "."/*
  do
    filename=${filename##*/} # remove extension
    if [[ "jupyter_execute" == *"$filename"* ]]
    then
        echo "removed jupyter_execute" | rm -r jupyter_execute
    fi
  done

# remove _website
ablog clean -D

sphinx-autobuild -a . ./_website      \
  --host 127.0.0.1 \
  --port=5002 \
  --open-browser \
  --re-ignore $PWD'/jupyter_execute/blog/(?!(?:.*/)?/[^/]*$).*' \
  --re-ignore $PWD'/.idea/(?!(?:.*/)?/[^/]*$).*' \
  --re-ignore $PWD'/.venv/(?!(?:.*/)?/[^/]*$).*' \
  --pre-build "ablog clean -D"


# reg-expression for files to ignore:
# - https://regex101.com/r/DZgfK6/2
# - https://stackoverflow.com/questions/51428249/regular-expressions-match-any-file-under-a-certain-directory-unless-the-leaf-d