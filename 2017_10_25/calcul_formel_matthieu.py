# -*- coding: utf-8 -*-
from math import sin, cos, pi

class Expr(object):
    def __init__(self, name):
        self.name = name
        
    def __add__(self,other):
        if isinstance(other, Expr):
            return Sum(self, other)
        return NotImplemented
    
    def __truediv__(self,other):
        if isinstance(other, Expr):
            return Div(self, other)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Expr):
            return Sub(self, other)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, Expr):
            return Mul(self, other)
        return NotImplemented
    
    def __neg__(self):
        return Mul(self, Number(-1))
    
    def simplify(self):
        return self
    
    def simplify0(self):
        return self
    
class Symbol(Expr):
    def display(self):
        return self.name
    
    def evaluate(self, **kwd):
        if self.name in kwd.keys():
            return(kwd[self.name])
        raise Exception("Ne peut évaluer la variable")
        
    def derivate(self, symbol):
        if self.name==symbol:
            return(Number(1))
        return(Number(0))
        
    def __eq__(self, other):
        if isinstance(other, Symbol):
            if self.name==other.name:
                return True
        return False
           
class Function(Expr):
    pass

class BinaryOperator(Function):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2
    
    def display(self):
        return("({left} {ope} ²{right})".format(left=self.expr1.display(), ope=self.ope,
                                              right=self.expr2.display()))    
    def __eq__(self, other):
        if isinstance(other, BinaryOperator):
            if self.ope==other.ope and self.expr1==other.expr1 and self.expr2==other.expr2:
                return True
        return False
        
    def simplify0(self):
        return self
    
    liste_methodes_simplifications = ['simplifyNumbers', 'simplify0']
    
    def simplify(self):
        simpleOld = self
        simpleNew = self.__class__(self.expr1.simplify(), self.expr2.simplify())
        for methode_name in self.liste_methodes_simplifications:
            simpleNew = getattr(simpleNew, methode_name)()
            if simpleNew!=self:
                return simpleNew.simplify()
        return simpleNew

#        while simpleOld!=simpleNew and isinstance(simpleNew, BinaryOperator):
#            simpleOld = simpleNew
#            simpleNew = simpleNew.__class__(simpleNew.expr1.simplify(), simpleNew.expr2.simplify())
##            simpleNew = simpleNew.simplifyNumbers()
##            simpleNew = simpleNew.simplify0()
#            for methode_name in self.liste_methodes_simplifications:
#                simpleNew = getattr(simpleNew, methode_name)()
#        return simpleNew
        
        
class Sum(BinaryOperator):
    ope='+'
#    opeName = Sum
           
    def evaluate(self, **kwd):
        return(self.expr1.evaluate(**kwd)+self.expr2.evaluate(**kwd))
        
    def derivate(self, symbol):
        return(self.expr1.derivate(symbol)+self.expr2.derivate(symbol))
        
    def simplifyNumbers(self):
        if isinstance(self.expr1, Number) and isinstance(self.expr2, Number):
            return Number(self.expr1.val + self.expr2.val)
        return self
    
    def simplify0(self):
        if self.expr1==Number(0):
            return self.expr2
        elif self.expr2==Number(0):
            return self.expr1
        return self
       
class Sub(BinaryOperator):
    ope='-'
    
    def evaluate(self, **kwd):
        return(self.expr1.evaluate(**kwd)-self.expr2.evaluate(**kwd))
        
    def derivate(self, symbol):
        return(self.expr1.derivate(symbol)-self.expr2.derivate(symbol))
        
    def simplifyNumbers(self):
        if isinstance(self.expr1, Number) and isinstance(self.expr2, Number):
            return Number(self.expr1.val - self.expr2.val)
        return self
    
    def simplify0(self):
        if self.expr1==Number(0):
            return -self.expr2
        elif self.expr2==Number(0):
            return self.expr1
        return self
        
class Mul(BinaryOperator):
    ope='*'
    
    def evaluate(self, **kwd):
        return(self.expr1.evaluate(**kwd)*self.expr2.evaluate(**kwd))
        
    def derivate(self, symbol):
        return(self.expr1.derivate(symbol)*self.expr2 + self.expr1*self.expr2.derivate(symbol))
        
    def simplify0(self):
        if self.expr1==Number(0) or self.expr2==Number(0):
            return Number(0)
        if self.expr1==Number(1):
            return self.expr2
        if self.expr2==Number(1):
            return self.expr1
        return self
    
    def simplifyNumbers(self):
        if isinstance(self.expr1, Number) and isinstance(self.expr2, Number):
            return Number(self.expr1.val * self.expr2.val)
        return self    
    
         
class Div(BinaryOperator):
    ope='/'
        
    def evaluate(self, **kwd):
        return(self.expr1.evaluate(**kwd)/self.expr2.evaluate(**kwd))
    
    def derivate(self, symbol):
        return(self.expr1.derivate(symbol)/self.expr2 
               - self.expr1*self.expr2.derivate(symbol)/(self.expr2*self.expr2))
    
    def simplifyNumbers(self):
        if isinstance(self.expr1, Number) and isinstance(self.expr2, Number):
            return Number(self.expr1.val / self.expr2.val)
        return self
        
    def simplify0(self):
        if self.expr1==Number(0):
            return Number(0)
        return self
    
    def simplify_same_expr(self):
        print('COUCOU')
        if self.expr1==self.expr2:
            return Number(1)
        return self

    liste_methodes_simplifications = BinaryOperator.liste_methodes_simplifications# + ['simplify_same_expr']
    
class MathFunction(Function):
    def __init__(self, expr):
        self.arg = expr
        
    def display(self):
        return '{self.function_name}({arg})'.format(self=self,
                   arg=self.arg.display())
        
    def evaluate(self, **kwd):
        return self.function_operator(self.arg.evaluate(**kwd))
    
           
class Number(MathFunction):
    def __init__(self, val):
        self.val = val
    
    def display(self):
        return str(self.val)
    
    def evaluate(self, **kwd):
        return self.val
    
    def derivate(self, symbol):
        return Number(0)
    
    def __eq__(self, other):
        if isinstance(other, Number):
            if self.val==other.val:
                return True
        return False
    
    def simplify(self):
        return self
       
class Sin(MathFunction):
    function_name = 'sin'
    function_operator = sin
   
    def derivate(self, symbol):
        return self.arg.derivate(symbol)*Cos(self.arg)
    
    def __eq__(self, other):
        if isinstance(other, Sin):
            if self.arg==other.arg:
                return True
        return False
    
    def simplify(self):
        return Sin(self.arg.simplify())
    
class Cos(MathFunction):
    function_name = 'cos'
    function_operator = cos
    
    def derivate(self, symbol):
        return -(self.arg.derivate(symbol)*Sin(self.arg))
    
    def __eq__(self, other):
        if isinstance(other, Cos):
            if self.arg==other.arg:
                return True
        return False
    
    def simplify(self):
        return Cos(self.arg.simplify())
    
x = Symbol('x')
y = Symbol('y')
expr = (Sin(x)/Cos(y))*Number(10)
print(x.display())
print(y.display())
print(expr.display())
print(expr.evaluate(x=pi/2,y=0))
print(expr.derivate('y').display())
print('magic simplified result!!!!!!!')
print(expr.derivate('y').simplify().display())
