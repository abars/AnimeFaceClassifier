#Separate dataset

use warnings;
use strict;
use File::Spec::Functions qw/catfile/;

my $sum = 0;
my $count = 0;

my $thumb_dir = "animeface-character-dataset/thumb";

mkdir "train";
mkdir "validation";

opendir(THUMB, $thumb_dir) or die "usage: $0 thumb_dir\n";
foreach my $dir (readdir(THUMB)) {
  next if ($dir eq '.' || $dir eq '..');
  next if ($dir eq '.DS_Store');
  my $tag_dir = catfile($thumb_dir, $dir);
  check($tag_dir,$dir);
}
close(THUMB);

printf("\npng: %d, folder: %d, avg: %f\n", $sum, $count, $sum /$count);

sub check
{
  my $dir = shift;
  my $id = shift;
  my $png_count = 0;
  my $ignore = 0;
  my $csv = 0;

  mkdir "train/$id";
  mkdir "validation/$id";
  
  opendir(D, $dir) or die "$dir: $!\n";
  foreach my $file (readdir(D)) {
    if ($file =~ /\.png$/) {
      ++$png_count;
      if($png_count%4!=0){
        system("cp $dir/$file train/$id/$file");
      }else{
        system("cp $dir/$file validation/$id/$file");
      }
    }
    if ($file eq 'ignore') {
      $ignore = 1;
    }
    if ($file eq 'color.csv') {
      $csv = 1;
    }
    
  }
  closedir(D);
  $sum += $png_count;
  ++$count;
  
  my $csv_size = -s catfile($dir, "color.csv");
  my $ok = 0;
  if ($ignore) {
    $ok =1;
  } else {
    if ($png_count > 0 && $csv && $csv_size > 0) {
      $ok = 1;
    }
  }
  
  printf("%s: %d, %d, %d: %s\n", $dir, $png_count, $csv, $ignore,
         ($ok ? "OK":"NG"));
}
