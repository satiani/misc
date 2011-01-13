#!/usr/bin/ruby

require 'net/http'

`rm -f *.pdf`

t = Time.now
date_str_query = t.strftime("%m/%d/%Y")
date_str_uri = t.strftime("%-d-%-m-%Y")
final_page = 0

Net::HTTP.start("www.al-ayyam.ps") { |http|
    resp = http.get("/znews/site/template/pdf.aspx?Date=#{date_str_query}")
    resp.body.scan(%r!a href=/znews/site/pdfs/#{date_str_uri}/p([0-9]+).pdf!) { |w|
        final_page = w[0].to_i
    }

    puts final_page
}

1.upto(final_page) { |i|
    `wget http://www.al-ayyam.ps/znews/site/pdfs/#{date_str_uri}/p#{"%02d" % i}.pdf`
}

`pdftk *.pdf cat output combined.pdf verbose`
