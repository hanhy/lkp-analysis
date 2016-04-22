use strict;
#  Author: Minghui Zhou
#
#Extract each revision from FreeBSD-release/10.2.0 log output
#

require "timelocal.pl";

my %paths = ();
my ($rev, $aname, $alogin, $atime, $cname, $clogin, $ctime, $comment) = ("","","","","","","","","","");
my ($getHeader, $getPaths) = (0, 0);

sub output {
	foreach my $f (keys %paths){
		$comment =~ s/\r/ /g;
		$comment =~ s/\;/SEMICOLON/g;
		$comment =~ s/\n/__NEWLINE__/g;
		print "$rev\;$aname\;$cname\;$alogin\;$clogin\;$paths{$f}\;$atime\;$ctime\;$f\;$comment\n";
	}
	%paths = ();
	($rev, $aname, $alogin, $atime, $cname, $clogin, $ctime, $comment) = ("","","","","","","","","","");
}


while(<STDIN>){
	chop ();	
	#catch end of last revision information
	if (/^STARTOFTHECOMMIT$/){
		&output ();
		$getHeader=1;$getPaths=0;
		next;
	}
	#process file header
	if ($getHeader){
		$_ =~ s/ \| /\|/g;
		($rev, $aname, $alogin, $atime, $cname, $clogin, $ctime, $comment) = split(/\;/, $_, -1);
		$getHeader = 0;
		$getPaths = 1;
		next;
		#print STDERR "getHeader $rev, $login, $date, $line\n"; 
	}
	if ($getPaths && /^$/){
		next;
	}
	if ($getPaths && /^[0-9]/){
		/(\d+)\s+(\d+)\s+(.*)$/;
		my ($nadd, $ndel, $path) = ($1, $2, $3);
		$paths{$path}="$nadd:$ndel";
	}
}

&output ();


