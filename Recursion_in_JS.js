//Recursion is hard in JavsScript
//details see https://www.cs.cmu.edu/~yandongl/recursion_in_js.html
function findParent(path, db, child, cb) {
  db.find({children:{$elemMatch:{id:child}}}).toArray(function (err, items) {
    var rs = [];
    if( items.length==0 ) {
      cb('no parent', path.slice(0));
    } else {
      async.eachSeries(items, function(e, cb1) {
        path.push(e.id);
        findParent(path, db, e.id, function(rs1){
          rs = rs.concat(rs1);
          path.pop();
          cb1();
        });
      }, function(err){
        if(err) console.log('async error.');
        cb(err, rs);
      });  
    }
  });
}
