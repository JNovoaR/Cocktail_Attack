use strict;

open(db_file, "<", @ARGV[0]) or die "Unable to open \"@ARGV[0]\" file";

my $sel_drug = @ARGV[1];
my $new_drug_coming = 0;
my $printing = 0;
my $pass = 0;
my $maybe_need_to_print = "";

while (<db_file>) {
	if ($pass ne 1) {	
		if ($_ =~ /^<drug type=/i) {
			$new_drug_coming = 1;
			$maybe_need_to_print = $_;
		}
		if ($_ =~ /<drugbank-id primary="true">(.*)<\/drugbank-id>/i) {
			my $drug_id = $1;
			
			if ($new_drug_coming eq 1) {
				if ($sel_drug eq $drug_id) {
					$printing = 1;
					print $maybe_need_to_print;
				}
				$new_drug_coming = 0;
			}
		}
		if ($printing eq 1) {
			print $_;
			if ($_ =~ /^<\/drug>/i) {
				$printing = 0;
				$pass = 1;
			}
		}
	}
}
