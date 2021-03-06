<?php
include_once('functions.php');
include_once("config.php");
include_once("institute_header.php");
include_once("institute_functions.php");
check_session();
if(isset($_POST['cand_id']) && isset($_POST['job_id']))
{
	$id=$_POST['cand_id'];
	echo $id;
	$jobid=$_POST['job_id'];
	$sql="select * from jobs where job_id='$jobid' and institute_id='$institute_id'";
	$res=mysqli_query($con,$sql);
	$row_job=mysqli_fetch_array($res);
	$sql2="select * from Candidates where ID='$id'";
	$result=mysqli_query($con,$sql2);
	if(!$result)
		die("Server is down.");
	$row=mysqli_fetch_array($result);
	$bits=explode(",/,",$row['Status_bits']);
	
	$im=base64_encode($row['Image']);
	$cand_name=ucwords($row['Name']);
	$barV=$row['Progress'];
	$qualis=explode(",/,",$row['Quali']);
	$degree=$row['Degree'];
	$exp_year=$row['Experience'];
	$course=$row['Course'];
	$p_year=$row['Passing_year'];
	$intern=$row['Intern'];
	$college=$row["College"];
	$col_pin=$row['College_pincode'];
	$postal_add=$row['Postal_Add'];
	$perm_add=$row['Perm_Add'];
	$per_pin=$row['Per_pincode'];
	$country=$row['Country'];
	$state=$row['State'];
	$city=$row['City'];
	$dob= date('d/m/Y', strtotime($row['DOB']));
	$gender=$row['Gender'];
	$updated=$row['isUpdated'];
	$desc=$row['Description'];
?>
<div class="container well">
    <div class="row">
       <div class="col-sm-1">
       	
       </div>
        <div class="col-sm-7">
            <h3><b>Job Title : <?php echo $row_job["job_title"]; ?></b></h3>
		</div>
		<div class="col-sm-4" >
		
		</div>
	</div>
	<hr style="border-width: 2px;border-color:rgba(180,180,180,1.00)"/>
	<div class="row">
       <div class="col-sm-1">
       <button class="btn btn-sm btn-primary" onclick="javascript:history.back()"><span class="glyphicon glyphicon-arrow-left"></span> Back</button>
       </div>
        <div class="col-sm-7">
            <div class="candidate_id" id="<?php echo $id; ?>">
           		<div class="media">
				<div class="media-left">
				  <img class="img-circle" style="height:150px;" src="data:image/jpeg;base64,<?php echo $im; ?>" />
				</div>
				<div class="media-body" style="line-height: 25px;">
			  <br/>
				  <h4><b><?php echo $cand_name; ?></b></h4>
				  <br/>
					<div class="progress" style="width:60%">
					<div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="<?php echo $barV; ?>" aria-valuemin="0" aria-valuemax="100" style="width:<?php echo $barV.'%'; ?>"><?php echo $barV.'%'; ?>
					</div>
				  	</div>
				  	
				</div>
			  </div>
            </div>
		</div>
		<div class="col-sm-4" >
		<div class="row" align="center" id="<?php echo $id; ?>">
		<?php 
				if(isset($_POST['app_id']))
				{
					$app_id=$_POST['app_id'];
					$q1="select status_bit from applications where application_id='$app_id' and institute_id='$institute_id'";
					$ex1=mysqli_query($con,$q1);
					$row1=mysqli_fetch_array($ex1);
					$status_bit=$row1['status_bit'];
					?><?php if($status_bit==-99){?>
					<button class="btn btn-success Accept" id="<?php echo $app_id;?>">Accept</button><?php  } else if($status_bit=='1'){ ?><button class="btn btn-success Accepted" readonly="true" disabled>Accepted</button><?php  } ?>
                	<button class="btn btn-danger Reject" id="<?php echo $$app_id;?>">Reject</button>
					<?php
				}
				else
				{
		?>
			<button class="btn btn-primary offer_status" id="send_offer" >Send a offer <span class="glyphicon glyphicon-send"></span></button>
			<?php
				}
			?>
		</div>
		</div>
	</div>
  <hr class="hr-primary" size='30'/>
  
</div>
<div class="modal fade" id="errorModal" role="dialog">
    <div class="modal-dialog">
      <div class="modal-content alert alert-danger alert-dismissable fade in">
        <div class="modal-body">
        <div><a href="#" class="close" data-dismiss="modal" aria-label="close">&times;</a>Try again!</div>
		</div>
	</div>
 </div> 
</div>
<div class="modal fade" id="offerModal" role="dialog">
    <div class="modal-dialog">
      <div class="modal-content alert alert-success alert-dismissable fade in">
        <div class="modal-body">
        <div><a href="#" class="close" data-dismiss="modal" aria-label="close">&times;</a>Offer sent, Successfully!</div>
		</div>
	</div>
 </div> 
</div>
<script>

</script>
<?php
}
?>
<?php 
include_once("institute_footer.php");
?>