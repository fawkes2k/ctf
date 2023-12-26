/* calculateChecksum(std::__1::vector<int, std::__1::allocator<int> > const&) */
void calculateChecksum(vector *param_1)
{
  bool bVar1;
  int *piVar2;
  basic_string abStack_98 [10];
  basic_string abStack_70 [7];
  int local_54;
  undefined8 local_50;
  undefined8 local_48;
  vector<> *local_40;
  basic_string<> abStack_38 [24];
  vector *local_20;

  local_20 = param_1;
  
  // Initialize an empty string
  __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B7v160006IDnEEPKc(abStack_38,"");
  
  local_40 = (vector<> *)local_20;
  
  // Get the beginning and end iterators of the vector
  local_48 = std::__1::vector<>::begin[abi:v160006]((vector<> *)local_20);
  local_50 = std::__1::vector<>::end[abi:v160006](local_40);
  
  // Iterate over the vector
  while (bVar1 = std::__1::operator!=[abi:v160006]<int_const*>
                           ((__wrap_iter *)&local_48,(__wrap_iter *)&local_50), bVar1) {
    // Get the value at the current iterator position
    piVar2 = (int *)std::__1::__wrap_iter<int_const*>::operator*[abi:v160006]
                              ((__wrap_iter<int_const*> *)&local_48);
    local_54 = *piVar2;
    
    // Convert the integer to a string and append it to the initialized string
    std::__1::to_string(local_54);
    std::__1::basic_string<>::operator+=[abi:v160006](abStack_38,abStack_70);
    std::__1::basic_string<>::~basic_string((basic_string<> *)abStack_70);
    
    // Move to the next iterator position
    std::__1::__wrap_iter<int_const*>::operator++[abi:v160006]((__wrap_iter<int_const*> *)&local_48);
  }
  
  // Initialize another empty string
  std::__1::basic_string<>::basic_string(abStack_98);
  
  // Call a function "sha256" with the string as an argument
  sha256((basic_string)abStack_98);
  
  // Cleanup: Destructors for the initialized strings
  std::__1::basic_string<>::~basic_string((basic_string<> *)abStack_98);
  std::__1::basic_string<>::~basic_string(abStack_38);
  
  return;
}
