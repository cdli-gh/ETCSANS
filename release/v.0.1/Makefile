all: core extended

core: core/royal core/parallel

core/royal: ../../dev/ETCSANS-core/royal
	mkdir -p core/royal
	for file in ../../dev/ETCSANS-core/royal/release/data/*.conll; do \
		dir=`basename $$file | sed s/'^\(....\).*'/'\1'/`;\
		if [ ! -e core/royal/$$dir ]; then \
			mkdir core/royal/$$dir; \
		fi;\
		if [ ! -e core/royal/$$dir/`basename $$file` ]; then \
			echo $$file ">" core/royal/$$dir 1>&2; \
			cp $$file core/royal/$$dir;\
		fi;\
	done;

core/parallel: ../../dev/ETCSANS-core/parallel/ core/royal
	# royal takes priority over parallel
	mkdir -p core/parallel
	for file in `find ../../dev/ETCSANS-core/parallel/consolidated | grep '.conll$$'`; do \
		dir=`basename $$file | sed s/'^\(....\).*'/'\1'/`;\
		if [ ! -e core/royal/$$dir/`basename $$file ` ]; then \
			if [ ! -e core/parallel/$$dir ]; then \
				mkdir core/parallel/$$dir; \
			fi;\
			if [ ! -e core/parallel/$$dir/`basename $$file` ]; then \
				echo $$file ">" core/parallel/$$dir 1>&2; \
				cp $$file core/parallel/$$dir;\
			fi;\
		fi;\
	done;

extended: core ../../dev/ETCSANS-extended/ur3_corpus_data
	# core takes priority over extended
	mkdir extended
	for dir in ../../dev/ETCSANS-extended/ur3_corpus_data/annotated/morph/*/; do \
		if [ ! -e extended/`basename $$dir` ]; then \
			mkdir extended/`basename $$dir`; \
		fi;\
		for file in $$dir/*conll; do \
			if [ ! -e core/*/`basename $$dir`/`basename $$file` ]; then \
				echo $$file ">" extended/`basename $$dir` 1>&2; \
				cp $$file extended/`basename $$dir`; \
			fi;\
		done;\
	done;\
