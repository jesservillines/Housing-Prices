{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "InternalHashError",
     "evalue": "module '__main__' has no attribute '__file__'\n\nWhile caching the body of `load_data()`, Streamlit encountered an\nobject of type `builtins.function`, which it does not know how to hash.\n\n**In this specific case, it's very likely you found a Streamlit bug so please\n[file a bug report here.]\n(https://github.com/streamlit/streamlit/issues/new/choose)**\n\nIn the meantime, you can try bypassing this error by registering a custom\nhash function via the `hash_funcs` keyword in @st.cache(). For example:\n\n```\n@st.cache(hash_funcs={builtins.function: my_hash_func})\ndef my_func(...):\n    ...\n```\n\nIf you don't know where the object of type `builtins.function` is coming\nfrom, try looking at the hash chain below for an object that you do recognize,\nthen pass that to `hash_funcs` instead:\n\n```\nObject of type builtins.function: <function load_data at 0x00000148C6A29160>\n```\n\nPlease see the `hash_funcs` [documentation]\n(https://streamlit.io/docs/caching.html)\nfor more details.\n            ",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\streamlit\\hashing.py\u001b[0m in \u001b[0;36mto_bytes\u001b[1;34m(self, obj, context)\u001b[0m\n\u001b[0;32m    288\u001b[0m             \u001b[1;31m# Hash the input\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 289\u001b[1;33m             \u001b[0mb\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34mb\"%s:%s\"\u001b[0m \u001b[1;33m%\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mtname\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_to_bytes\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mobj\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    290\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\streamlit\\hashing.py\u001b[0m in \u001b[0;36m_to_bytes\u001b[1;34m(self, obj, context)\u001b[0m\n\u001b[0;32m    544\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 545\u001b[1;33m             \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_file_should_be_hashed\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mobj\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__code__\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mco_filename\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    546\u001b[0m                 \u001b[0mcontext\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_get_context\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mobj\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\streamlit\\hashing.py\u001b[0m in \u001b[0;36m_file_should_be_hashed\u001b[1;34m(self, filename)\u001b[0m\n\u001b[0;32m    323\u001b[0m         return file_util.file_is_in_folder_glob(\n\u001b[1;32m--> 324\u001b[1;33m             \u001b[0mfilepath\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_get_main_script_directory\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    325\u001b[0m         ) or file_util.file_in_pythonpath(filepath)\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\streamlit\\hashing.py\u001b[0m in \u001b[0;36m_get_main_script_directory\u001b[1;34m()\u001b[0m\n\u001b[0;32m    626\u001b[0m         \u001b[1;31m# script path in ScriptRunner.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 627\u001b[1;33m         \u001b[0mmain_path\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m__main__\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__file__\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    628\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdirname\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmain_path\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: module '__main__' has no attribute '__file__'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mInternalHashError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-dbe7486b8854>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     19\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     20\u001b[0m \u001b[1;33m@\u001b[0m\u001b[0mst\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcache\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 21\u001b[1;33m \u001b[1;32mdef\u001b[0m \u001b[0mload_data\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     22\u001b[0m     \u001b[0mdf\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'data/austen_poe.csv'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     23\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mdf\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\streamlit\\caching.py\u001b[0m in \u001b[0;36mcache\u001b[1;34m(func, persist, allow_output_mutation, show_spinner, suppress_st_warning, hash_funcs, max_entries, ttl)\u001b[0m\n\u001b[0;32m    498\u001b[0m     \u001b[1;31m# because this step will be hashing any objects referenced in the function\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    499\u001b[0m     \u001b[1;31m# body.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 500\u001b[1;33m     update_hash(\n\u001b[0m\u001b[0;32m    501\u001b[0m         \u001b[0mfunc\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    502\u001b[0m         \u001b[0mhasher\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mfunc_hasher\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\streamlit\\hashing.py\u001b[0m in \u001b[0;36mupdate_hash\u001b[1;34m(val, hasher, hash_reason, hash_source, context, hash_funcs)\u001b[0m\n\u001b[0;32m     88\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     89\u001b[0m     \u001b[0mch\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_CodeHasher\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mhash_funcs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 90\u001b[1;33m     \u001b[0mch\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mhasher\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mval\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     91\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     92\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\streamlit\\hashing.py\u001b[0m in \u001b[0;36mupdate\u001b[1;34m(self, hasher, obj, context)\u001b[0m\n\u001b[0;32m    312\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mupdate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mhasher\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mobj\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    313\u001b[0m         \u001b[1;34m\"\"\"Update the provided hasher with the hash of an object.\"\"\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 314\u001b[1;33m         \u001b[0mb\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mto_bytes\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mobj\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    315\u001b[0m         \u001b[0mhasher\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mb\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    316\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\streamlit\\hashing.py\u001b[0m in \u001b[0;36mto_bytes\u001b[1;34m(self, obj, context)\u001b[0m\n\u001b[0;32m    301\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    302\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mBaseException\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 303\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mInternalHashError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0me\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mobj\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    304\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    305\u001b[0m         \u001b[1;32mfinally\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\streamlit\\hashing.py\u001b[0m in \u001b[0;36mto_bytes\u001b[1;34m(self, obj, context)\u001b[0m\n\u001b[0;32m    287\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    288\u001b[0m             \u001b[1;31m# Hash the input\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 289\u001b[1;33m             \u001b[0mb\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34mb\"%s:%s\"\u001b[0m \u001b[1;33m%\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mtname\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_to_bytes\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mobj\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    290\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    291\u001b[0m             \u001b[1;31m# Hmmm... It's possible that the size calculation is wrong. When we\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\streamlit\\hashing.py\u001b[0m in \u001b[0;36m_to_bytes\u001b[1;34m(self, obj, context)\u001b[0m\n\u001b[0;32m    543\u001b[0m             \u001b[0mh\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mhashlib\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnew\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"md5\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    544\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 545\u001b[1;33m             \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_file_should_be_hashed\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mobj\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__code__\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mco_filename\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    546\u001b[0m                 \u001b[0mcontext\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_get_context\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mobj\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    547\u001b[0m                 \u001b[1;32mif\u001b[0m \u001b[0mobj\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__defaults__\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\streamlit\\hashing.py\u001b[0m in \u001b[0;36m_file_should_be_hashed\u001b[1;34m(self, filename)\u001b[0m\n\u001b[0;32m    322\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[1;32mFalse\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    323\u001b[0m         return file_util.file_is_in_folder_glob(\n\u001b[1;32m--> 324\u001b[1;33m             \u001b[0mfilepath\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_get_main_script_directory\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    325\u001b[0m         ) or file_util.file_in_pythonpath(filepath)\n\u001b[0;32m    326\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\streamlit\\hashing.py\u001b[0m in \u001b[0;36m_get_main_script_directory\u001b[1;34m()\u001b[0m\n\u001b[0;32m    625\u001b[0m         \u001b[1;31m# This works because we set __main__.__file__ to the report\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    626\u001b[0m         \u001b[1;31m# script path in ScriptRunner.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 627\u001b[1;33m         \u001b[0mmain_path\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m__main__\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__file__\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    628\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdirname\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmain_path\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    629\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mInternalHashError\u001b[0m: module '__main__' has no attribute '__file__'\n\nWhile caching the body of `load_data()`, Streamlit encountered an\nobject of type `builtins.function`, which it does not know how to hash.\n\n**In this specific case, it's very likely you found a Streamlit bug so please\n[file a bug report here.]\n(https://github.com/streamlit/streamlit/issues/new/choose)**\n\nIn the meantime, you can try bypassing this error by registering a custom\nhash function via the `hash_funcs` keyword in @st.cache(). For example:\n\n```\n@st.cache(hash_funcs={builtins.function: my_hash_func})\ndef my_func(...):\n    ...\n```\n\nIf you don't know where the object of type `builtins.function` is coming\nfrom, try looking at the hash chain below for an object that you do recognize,\nthen pass that to `hash_funcs` instead:\n\n```\nObject of type builtins.function: <function load_data at 0x00000148C6A29160>\n```\n\nPlease see the `hash_funcs` [documentation]\n(https://streamlit.io/docs/caching.html)\nfor more details.\n            "
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import pickle\n",
    "import streamlit as st\n",
    "\n",
    "st.set_page_config(\n",
    "    page_icon='📖',\n",
    "    initial_sidebar_state='expanded'\n",
    ")\n",
    "\n",
    "st.title('Ames Predict-O-Matic!')\n",
    "\n",
    "st.write('Use the sidebar to select a page to view.')\n",
    "\n",
    "page = st.sidebar.selectbox(\n",
    "    'Page',\n",
    "    ('Home', 'Form')\n",
    ")\n",
    "\n",
    "@st.cache\n",
    "def load_data():\n",
    "    df = pd.read_csv('data/austen_poe.csv')\n",
    "    return df\n",
    "\n",
    "if page == 'Home':\n",
    "    st.subheader('Home Page')\n",
    "    st.write('Hello, World, to my sliiiiick Streamlit App!')\n",
    "    \n",
    "if page == 'Form':\n",
    "    # header\n",
    "    st.subheader('Home Qualities')\n",
    "    st.write('''Input the qualities of the home\n",
    "    for which you want the price predicted.''')\n",
    "    \n",
    "    # get user input\n",
    "    qual = st.number_input('Overall Quality', format='%d', min_value=int(0), value=int(0))\n",
    "    bath = st.number_input('Number of Bathrooms', format='%d', min_value=int(0), value=int(0))\n",
    "    garage = st.number_input('Garage Area', format='%d', min_value=int(0), step=100, value=int(0))\n",
    "    lot = st.number_input('Lot Area', format='%d', min_value=int(0), step=1000, value=int(0))\n",
    "\n",
    "    data = np.array([qual, bath, garage, lot]).reshape(1, -1)\n",
    "\n",
    "    st.subheader('Make a prediction')\n",
    "\n",
    "    with open('./model/model.p', 'rb') as pickle_in:\n",
    "        model = pickle.load(pickle_in)\n",
    "\n",
    "    predicted_price = model.predict(data)[0]\n",
    "\n",
    "    st.subheader('Results:')\n",
    "    st.write(f'Your home is worth {round(predicted_price, 2)}. Go you!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
