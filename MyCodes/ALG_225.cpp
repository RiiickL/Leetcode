#pragma once
#include "leetcode_comm.h"
#include <queue>

class MyStack {
public:
    queue<int> myqueue;
    /** Initialize your data structure here. */
    MyStack() {

    }

    /** Push element x onto stack. */
    void push(int x) {
        myqueue.push(x);
    }

    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int size = myqueue.size();
        int front_num = 0;
        for (int loop = 0; loop < size-1; loop++) {
            front_num = myqueue.front();
            myqueue.pop();
            myqueue.push(front_num);
        }
        front_num = myqueue.front();
        myqueue.pop();
        return front_num;
    }

    /** Get the top element. */
    int top() {
        int size = myqueue.size();
        int front_num = 0;
        for (int loop = 0; loop < size; loop++) {
            front_num = myqueue.front();
            myqueue.pop();
            myqueue.push(front_num);
        }
        return front_num;
    }

    /** Returns whether the stack is empty. */
    bool empty() {
        return myqueue.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */