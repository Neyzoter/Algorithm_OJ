/*
 * IntegerReverse.h
 *
 *  Created on: 2018年9月12日
 *      Author: HP528
 */

#ifndef INTEGERREVERSE_H_
#define INTEGERREVERSE_H_

#include <vector>
#include <cmath>
using namespace std;

class Solution_IntegerReverse {
public:
    int reverse(int x) {
    	if(x==0){
    		return 0;
    	}
    	vector<int> vec,vec_limit;
    	int remainder,quotient;
    	quotient = x;
    	while(quotient!=0){
    		remainder = quotient % 10;
    		quotient /= 10;
    		vec.push_back(remainder>=0?remainder:-remainder); //取正数
    	}
		//最小的数存成向量
		if(x<0){//加入个位
			vec_limit.push_back(0x7FFFFFFF % 10 +1);
		}
		else{
			vec_limit.push_back(0x7FFFFFFF % 10);
		}
		quotient = 0x7FFFFFFF / 10;//个位先剔除
		while(quotient!=0){
			remainder = quotient % 10;
			quotient /= 10;
			vec_limit.push_back(remainder);
		}

		vector<int>::const_iterator vec_iterator=vec.begin();
		int rtn = 0;
		if(vec.size()<vec_limit.size()){
			int pow_num=vec.size()-1;
			while(vec_iterator!=vec.end()){
				rtn += (*vec_iterator)*pow(10,pow_num);
				vec_iterator++;
				pow_num--;
			}
		}
		else{
			vec_iterator=vec.begin();
			vector<int>::const_iterator vec_limit_iterator=vec_limit.end()-1;
			int pow_num=vec.size()-1;
			int big_flag = 0;
			while(vec_iterator!=vec.end()){
				if(big_flag == 0 && *vec_iterator>*vec_limit_iterator){
					return 0;
				}
				else if(*vec_iterator<*vec_limit_iterator){
					big_flag = 1;
				}
				rtn += *vec_iterator*pow(10,pow_num);
				vec_iterator++;vec_limit_iterator--;pow_num--;
			}
		}
		return x>0?rtn:-rtn;
    }
};



#endif /* INTEGERREVERSE_H_ */
