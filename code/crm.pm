package crm;

require Exporter;
@ISA = qw (Exporter);
@EXPORT = qw(stmp2date toDay toWeek prevWeek toYear toMonth ccDateToStmp
				 textToStmp textToStmpYYMMDD textToStmpSMBS simpBuild simpProd
				 verify getMrBuild
				 maxTime maxTime1 fromDate toDate extension selectWindow
				 stmpToYM stmpToYW);

require "timelocal.pl";

$maxTime=3600*24*5;
$maxTime1=3600*24*1;
$fromDate	=1009861200; #Jan 1, 2002
$toDate		=10400000000;#infinity
$extension = "medium";
sub selectWindow {
	my($choice)=@_[0];
	if ($choice eq "large"){
		$extension="large";
		$fromDate  = 978325200; #Jan 1, 2001
		$fromDate  += 3600*24*365.25/2; # July 15, 2001
		$fromDate  += 3600*24*365.25; # July 15, 2002
	}
	if ($choice eq "small"){
		$extension="small";
		$fromDate  =1014958800; #Mar 1, 2002
	}
	if ($choice eq "tiny"){
		$extension="tiny";
		$fromDate  =1030852800; #Sep 1, 2002
	}
}

my @mmmmonths=("JAN","FEB","MAR","APR","MAY",
"JUN","JUL","AUG","SEP","OCT","NOV","DEC");
foreach $i (0 .. $#mmmmonths){
	$m2o{$mmmmonths[$i]}=$i;
}
1;

sub toDay {
	#converts timestamp to the 0AM of before that time
	my ($stmp)=@_[0];
	if ($stmp ne "" && $stmp != 0){
		my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst)=localtime($stmp);
		$stmp=$stmp-3600*$hour-60*$min-$sec;
	}
	$stmp;
}	
sub toWeek {
	#converts timestamp to the 0AM of first sunday before that time
	my ($stmp)=@_[0];
	if ($stmp ne "" && $stmp != 0){
		my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst)=localtime($stmp);
		$stmp=$stmp-3600*24*$wday-3600*$hour-60*$min-$sec;
	}
	$stmp;
}	

sub prevWeek {
	#converts timestamp to the 0AM of first sunday before that time
	my ($stmp,$n)=@_;
	if ($stmp ne "" && $stmp != 0){
		my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst)=localtime($stmp);
		my($stmp1)=$stmp-3600*24*$wday-3600*$hour-60*$min-$sec - $n*7*24*3600;
		my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst1)=localtime($stmp1);
		if ($isdst1 != $isdst){
			#print STDERR "$stmp1\;$stmp\;$isdst1\;$isdst\n";
			if ($isdst1){
				$stmp1-=3600;
			}else{
				$stmp1+=3600;
			}
		}
		 
		$stmp=$stmp1;
	}	
	$stmp;
}	

sub toYear {
	#converts timestamp to the 0AM of first sunday before that time
	my ($stmp)=@_[0];
	if ($stmp ne "" && $stmp != 0){
		my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst)=localtime($stmp);
		$stmp-3600*24*$yday-3600*$hour-60*$min-$sec;
	}else{
		$stmp;
	}
}


sub toMonth {
	#converts timestamp to the 0AM of first sunday before that time
	my ($stmp)=@_[0];
	if ($stmp ne "" && $stmp != 0){
		my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst)=localtime($stmp);
		$stmp-3600*24*$mday-3600*$hour-60*$min-$sec;
	}else{
		$stmp;
	}
}

sub ccDateToStmp {
	my ($date)=@_[0];
	$date =~ m/^[0-9][0-9]([0-9][0-9])([0-9][0-9])([0-9][0-9])\.([0-9][0-9])([0-9][0-9])([0-9][0-9])$/;
	my ($y,$m,$d,$h,$min,$s)=($1,$2,$3,$4,$5,$6);
	timelocal($s,$min,$h,$d,$m-1,$y);
}

sub textToStmpYYMMDD {
	my ($input)=@_[0];
	my ($dat,$tim)=split(/ /,$input);
	my ($y,$m,$dd)=split(/[\-\/]/,$dat);	
	my ($res)=0;
	if ($y eq ""){
		$res=0;
	}else{
		my $adjust = 0;
		if ($y == 37){
			$y = 1;
			$adjust = -3600*24*26; # go back 26 days
		}
		if ($y < 80){ $y=$y+100;} # for 00, 01, 02
		$y=$y+1900 if $y < 1900;
		if ($m !~ /[0-9]/){
			$m =~ tr/[a-z]/[A-Z]/;
			$m=$m2o{$m};
		}else{
			$m--;
		}
		my($h,$min,$s)=split(/\:/,$tim);;
		#print STDERR "$input\;$dd,$m,$y\n";
		$res=&timelocal($s+0,$min+0,$h+0,$dd+0,$m+0,$y)+$adjust;
	}
	$res;
}

sub textToStmpSMBS {
	my ($input)=@_[0];
	my ($dat,$tim)=split(/ /,$input);
	my ($m,$dd,$y)=split(/[\-\/]/,$dat);
	my ($res)=0;
	if ($y eq ""){
		$res=0;
	}else{
		my $adjust = 0;
		if ($y == 37){
			$y = 1;
			$adjust = -3600*24*26; # go back 26 days
		}
		$y=$y+100 if ($y < 80);
		$y=$y+1900 if ($y < 1900);
		if ($m !~ /[0-9]/){
			$m =~ tr/[a-z]/[A-Z]/;
			$m=$m2o{$m};
		}else{
			$m--;
		}
		my($h,$min,$s)=split(/\:/,$tim);;
		#print STDERR "$input\;$dd,$m,$y\n";
		$res=&timelocal($s+0,$min+0,$h+0,$dd+0,$m+0,$y)+$adjust;
	}
	$res;
}

#Wednesday 6:51 PM
#05/Mar/10 03:11 PM
sub textToStmp {
	my ($input)=@_[0];
	my ($dat,$tim)=split(/ /,$input);
	my ($dd,$m,$y)=split(/[\-\/]/,$dat);
	my ($res)=0;
	if ($y eq ""){
		$res=0;
	}else{
		my $adjust = 0;
		if ($y == 37){
			$y = 1;
			$adjust = -3600*24*26; # go back 26 days
		}
		$y=$y+100 if ($y < 80);
		$y=$y+1900 if ($y < 1900);
		if ($m !~ /[0-9]/){
			$m =~ tr/[a-z]/[A-Z]/;
			$m=$m2o{$m};
		}else{
			$m--;
		}
		my($h,$min,$s)=split(/\:/,$tim);;
		$res=&timelocal($s+0,$min+0,$h+0,$dd+0,$m+0,$y)+$adjust;
	}
	$res;
}

sub stmp2date {
	my ($stmp)=@_[0];
	my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst)=localtime($stmp);
	$mon++;
	if ($mon < 10){$mon = "0$mon";} 
	if ($mday < 10){$mday = "0$mday";} 
	(1900+$year).$mon.$mday;
}

sub simpBuild { #this is for the build version names in defect table
	my ($rel,$prod)=@_;
	#print STDERR ":$rel,$prod:\n";
	my $rel1 = $rel;
	if ($prod eq "QeS"){
		if ($rel =~ /Future/){ $rel1="QeS Future";}	
		if ($rel =~ /^IC 7\.Next/ || $rel =~ /^7\.next/){ $rel1="QeS 7.0.x";}	
		if ($rel =~ /^8\.1 |^IC 8\.1/){ $rel1="QeS 8.1";}	
		if ($rel =~ /^8\.0 |^IC 8\.0/){ $rel1="QeS 8.0";}	
		if ($rel =~ /^7\.1 |^IC 7\.1/){ $rel1="QeS 7.1";}	
		if ($rel =~ /^7\.0 |^IC 7\.0|ThinClient|Thin Client/){ $rel1="QeS 7.0";}	
		if ($rel =~ /^6\.1\.[34] |^IC 6\.1\.[34] /){ $rel1="QeS 6.1.3";}	
		if ($rel =~ /^6\.1 |^6\.1\.[12] /){ $rel1="QeS 6.1";}		
		if ($rel =~ /^6\.0/){
			if ($rel =~ /^6\.0 /){	$rel1="QeS 6.0"; }
			if ($rel =~ /^6\.0i /){	$rel1="QeS 6.0.1"; }
			if ($rel =~ /^6\.0\.([0-9]) /){	$rel1="QeS 6.0.$1"; }
		}elsif ($rel =~ /^5\.6/){ $rel1="QeS 5.6";}
		elsif ($rel =~ /^5\.5/ || $rel =~ /QeS 5.5/ || $rel =~ /Tradewind/){ $rel1="QeS 5.5";}
		elsif ($rel =~ /^QeS 5\.1|^5\.1 /){ $rel1="QeS 5.1";}
		elsif ($rel =~ /^QES 5\.0|^5\.0 /){ $rel1="QeS 5.0";}
		elsif ($rel =~ /^QES 4\./){ $rel1="QeS 4.0";}
		#elsif ($rel =~ /^CQ 3\./){ $rel1="QeS 3.0";}
	}
	$rel1;
}
sub simpProd { #this is for the product in the calls table
	my ($prod)=@_;
	my $prod1 = $prod;
	$prod1="QeS 6.1" if ($prod =~ /IC 6\.1/);
	$prod1="QeS 6.1.3" if $prod =~ /IC 6\.1\.3/;
	$prod1="QeS 6.0.2" if ($prod =~ /IC 6\.0\.2/);
	$prod1="QeS 6.0.1" if ($prod =~ /IC 6\.0\.1/);
	$prod1="QeS 5.6" if ($prod =~ /IC 5.6/);
	$prod1="QeS 5.6" if ($prod =~ /QeS 5.6/);
	$prod1="QeS 5.5" if ($prod =~ /QeS 5.5/);
	$prod1="QeS 5.1" if ($prod =~ /QeS 5.1/);
	$prod1="QeS 4.0" if ($prod =~ /QES 5.1/);

	$prod1;
}
	

sub verify {
	my ($rel,$where,$stmp)=@_;
	if ($stmp ne "" && $stmp != 0){
		my ($y)=$stmp/365.25/3600/24+1970;
		if ($what ne "qq"){
			if ($rel eq "QeS 5.0" && $y >= 1999.37976886709){
				$rel="late$rel";
			}elsif ($rel eq "QeS 5.1" && $y < 1999.37976886709){
				$rel="early$rel";
			}elsif ($rel eq "QeS 5.1" && $y >= 1999.61255117626){
				$rel="late$rel";
			}elsif ($rel eq "QeS 5.5" && $y < 1999.61255117626){
				$rel="early$rel";
			}elsif ($rel eq "QeS 5.5" && $y >= 2000.70409951961){
				$rel="late$rel";
			}elsif ($rel eq "QeS 5.6" && $y < 2000.70409951961){
				$rel="early$rel";
			}elsif ($rel eq "QeS 5.6" && $y >= 2001.56425992471){
				$rel="late$rel";
			}elsif ($rel eq "QeS 6.0" && $y < 2001.56425992471){
				$rel="early$rel";
			}
		}
	}
	($rel,$where);	
}

sub getMrBuild {
	local ($mr,$label)=@_;
	$mr = uc($mr);
	my ($rel,$where) = ("nomr","");
	my %rels=();
	if ($mr ne ""){
		my (@mrs)=();
		if ($mr=~/,/){
			@mrs=split(/,/,$mr);			
		}else{
			push @mrs, $mr;
		}
		if ($mr ne ""){
			foreach $mr1 (@mrs){
				if ($mr1 ne ""){ #skip empy entries
					if ($mr2data{$mr1} eq ""){
						# no valid MR in qq
					}else{
						my ($rel,@rest)=split(/\;/,$mr2data{$mr1});
						$rels{$rel}++;
						$where="qq";
					}
				}
			}
		}
	}
	
	if ($where eq "" && $label ne ""){
		if ("$label" =~ /QES_4\./){	$rel="QeS 4.0"; }
		elsif ("$label" =~ /QES_5\.0/){ $rel="QeS 5.0"; }
		elsif ("$label" =~ /QES_5\.1/){ $rel="QeS 5.1"; }
		elsif ("$label" =~ /ECONTACT55/){ $rel="QeS 5.5";}
		elsif ("$label" =~ /ECONTACT56/){ $rel="QeS 5.6"; }
		elsif ("$label" =~ /AIC60_BUILD/){$rel="QeS 6.0"; }
		if ($rel ne "nomr"){
			$where="label";
			$rels{$rel}++;
		}
	}
	if ($where ne ""){
		$rel=join ",",keys %rels;
		if ($rel=~/,/){
			print STDERR "multiple build per $mr\;$rel\n";
		}
	}
	($rel,$where);
}

sub stmpToYM {
        my ($stmp)=@_[0];
   if ($stmp ne "" && $stmp != 0){
     my ($s,$min,$h,$mday,$m,$y,$wday,$yday,$isdst)=localtime($stmp);
          $m ++;
          $m = "0$m" if ($m < 10);
          $y += 1900;
          $m =~ s/ //g;
          return ("$y $m");
  }else{
          return ("");
  }
}

sub stmpToYW {
        my ($stmp)=@_[0];
   if ($stmp ne "" && $stmp != 0){

     my ($s,$min,$h,$mday,$m,$y,$wday,$yday,$isdst)=localtime($stmp);
          my ($s1,$min1,$h1,$mday1,$m1,$y1,$wday1,$yday1,$isdst1) = localtime(timelocal(0,0,0,1,0,$y));
          my $week = int(($yday-$wday)/7)+1;
          $week = "0$week" if ($week < 10);
          $y += 1900;
          $week =~ s/ //g;
          return ("$y $week");
  }else{
          return ("");
  }
}

