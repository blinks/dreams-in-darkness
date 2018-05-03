push : dreams.pdf buildnumber.txt
	butler push --if-changed --userversion-file=buildnumber.txt \
		dreams.pdf blinks/dreams:book


dreams.pdf : README.asciidoc buildnumber.txt
	asciidoctor-pdf README.asciidoc -o dreams.pdf

buildnumber.txt : README.asciidoc
	echo `git describe --tags` > buildnumber.txt

.PHONY: push clean

clean :
	rm dreams.pdf buildnumber.txt
