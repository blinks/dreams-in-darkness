docs/index.html : README.asciidoc
	asciidoctor README.asciidoc -D docs -o index.html
