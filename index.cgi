#!/usr/bin/env perl

use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use Data::Dumper;

my $cgi = new CGI;

my %return_HTMLs = ();
my $mainHTMLs = '';
my $outpid;
my $grep_id;

print "Content-type: text/html; charset=utf-8;\n\n";

print << '__HTML__';

  <head>
    <title>Hello, world</title>

  </head>
  <body>
 <script src="./main.js"></script>
<form method="POST" action= "index.cgi" onClick="Calc();">
<h1>計算機(Sum Only)</h1>
      <input type= "text" id="inputL">
      +
      <input type= "text" id="inputR">
      <input type="button"  value="Submit" >
  <h2>結果</h2>

</form>

  <div id="result"></div>
  </body>

__HTML__
