#!/usr/bin/perl 

# convert cfg into cnf

$file = "grammar.cfg";
$fileout = 'grammar.cnf';
open(FILE, $file);
open(FILEOUT, ">$fileout");

	while(<FILE>) {
	chop;
        $rule[$i] = $_;
	$len[$i] = length($rule[$i]);
# fix the NOM stuff right off the bat
	$rule[$i] =~ s/Nom/NP/g;
	$rule[$i] =~ s/NNP/NP/g;
	$rule[$i] =~ s/NNS/NP/g;
	$rule[$i] =~ s/NN/NP/g;
	$rule[$i] =~ s/PRP/NP/g;
	$rule[$i] =~ s/Pro/NP/g;
	if($rule[$i] =~ /^#/){
	$flag[$i] = -1;}
	if($len[$i] == 0){$flag[$i] = -1;}
	if($flag[$i] == 0){$count++;
	$rules[$k] = $rule[$i];
	$k++;
	}
	#printf("%3d %2d %2d %s\n",$count,$flag[$i],$len[$i],$rule[$i]);
        $i++;
        }

# do a rule count
	for($i=0;$i<@rules;$i++){
	@ary = split(" ",$rules[$i]);
        if($rules[$i] =~ /'/){
	$nflag[$i] = 1;}

	$rule = "$ary[0]:";
	#if($nflag[$i] == 0){
	$lhs{$ary[0]}++;
        push(@{$rhs_rule{$ary[0]}},$rules[$i]);
	for($k=2;$k<@ary;$k++){
	$rhs{$ary[$k]}++;
	$rule = $rule . " " . $ary[$k];
	#}
	}
        #print "$rules[$i] $#ary : $rule\n";
	push(@{$types{$#ary-1}},$rule);
	}

# generate rules for terminals
print "Terminals\n";
        for($i=0;$i<@{$types{1}};$i++){
	$wflag[$i] = 0;
        if($types{1}[$i] =~ /'/){
	$wflag[$i] = 1;}
	#printf("%3d %2d %s\n",$i,$wflag[$i],$types{1}[$i]);
	}
$kk=0;
print "2s\n";
# existing binaries
       	for($i=0;$i<@{$types{2}};$i++){
	#print FILEOUT "$types{2}[$i]\n";
	$new_rules[$kk] = $types{2}[$i];
	$kk++;
        printf("%3d %2d %s\n",$i,$wflag[$i],$types{2}[$i]);
        }

print "3s\n";
# triples
        for($i=0;$i<@{$types{3}};$i++){
        printf("%3d %2d %s\n",$i,$wflag[$i],$types{3}[$i]);
        }


print "4s\n";
# quads
        for($i=0;$i<@{$types{4}};$i++){
        printf("%3d %2d %s\n",$i,$wflag[$i],$types{4}[$i]);
        }

print "3s\n\n";
	$l = 1;
        for($i=0;$i<@{$types{3}};$i++){
	print "$i $types{3}[$i]\n";
	($lhs,$rhs) = split(":",$types{3}[$i]);
	@ary = split(" ",$rhs);
	$new_rule[$l] = "X$l";
	$long1[$l]  = $lhs . ": " . $new_rule[$l] . " " .  $ary[$#ary];
	$long2[$l]  = $new_rule[$l] . ": " . $ary[0] . " ".  $ary[1];
	print "$long1[$l]\n";
	#print FILEOUT "$long1[$l]\n";
        $new_rules[$kk] = $long1[$l];
        $kk++;
	print "$long2[$l]\n\n";
	#print FILEOUT "$long2[$l]\n";
        $new_rules[$kk] = $long2[$l];
        $kk++;
	$l++;
	}

print "4s\n\n";
        for($i=0;$i<@{$types{4}};$i++){
        print "$i $types{4}[$i]\n";
        ($lhs,$rhs) = split(":",$types{4}[$i]);
        @ary = split(" ",$rhs);
        $new_rule[$l] = "X$l";
        $olong1[$l]  = $lhs . ": " . $new_rule[$l] . " " .  $ary[$#ary];
        #print FILEOUT "$olong1[$l]\n";
        $new_rules[$kk] = $olong1[$l];
        $kk++;
	$l++;
        $new_rule[$l] = "X$l";
        $long2[$l]  = $new_rule[$l-1] . ": " . $new_rule[$l] . " " .  $ary[$#ary-1];
        $long3[$l]  = $new_rule[$l] . ": " . $ary[0] . " ".  $ary[1];
        #print FILEOUT "$long2[$l]\n";
        $new_rules[$kk] = $long2[$l];
        $kk++;
        print "c:$long3[$l]\n\n";
        #print FILEOUT "$long3[$l]\n";
        $new_rules[$kk] = $long3[$l];
        $kk++;
        $l++;
        }	


print "Unit Productions\n";

        for($i=0;$i<@{$types{1}};$i++){
        if($wflag[$i] == 0){
        ($lhs,$rhs) = split(" ",$types{1}[$i]);
	$lhs =~ s/://;
	#print "$lhs - $rhs\n";

        #printf("%3d %2d - %2d:%2d - %s\n",$i,$wflag[$i],$lhs{$rhs},$rhs{$lhs},$types{1}[$i]);
        }}


# dump out all rules by lhs

	foreach $rule (sort keys %lhs){
	        for($i=0;$i<@{$rhs_rule{$rule}};$i++){
		#printf("%-8s %2d %s\n",$rule,$lhs{$rule},$rhs_rule{$rule}[$i]);
		}
	#print "\n";
	}

# terminals
        for($i=0;$i<@{$types{1}};$i++){
	if($wflag[$i] == 1){
	#print FILEOUT "$types{1}[$i]\n"; 	
        $new_rules[$kk] = $types{1}[$i];
	$kk++;
# adjective fix - deal with ADJP => ADJ
	if($types{1}[$i] =~ /Adj/){
	($a,$b) = split(" ",$types{1}[$i]);
	$temp = sprintf("ADJP: %s",$b);
	#print FILEOUT "$temp\n";
        $new_rules[$kk] = $temp;
        $kk++;}

# adverb fix - deal with ADVP => ADV
        if($types{1}[$i] =~ /Adv/){
        ($a,$b) = split(" ",$types{1}[$i]);
        $temp = sprintf("ADVP: %s",$b);
        #print FILEOUT "$temp\n";
        $new_rules[$kk] = $temp;
        $kk++;}

	}}

#unit fixes
	# deal with this unit mapping - it's a little lame
	$temp = "NP: 'There'";
        #print FILEOUT "$temp\n";
        $new_rules[$kk] = $temp;
        $kk++;

# prep output file for Johnny's CKY routine
    print FILEOUT "\(\n";
	for($i=0;$i<@new_rules;$i++){
	@ary = split(" ",$new_rules[$i]);
	$ary[0] =~ s/://;
	if($#ary == 2){
	$temp = sprintf("\('%s',\('%s','%s'\)\),",$ary[0],$ary[1],$ary[2]);}
	else {
	$temp = sprintf("\('%s',%s),",$ary[0],$ary[1]);
	}
	print "   $temp\n";
	print FILEOUT "   $temp \n";
	}
	print FILEOUT "\)";
	
