# Generated from PythonSubset.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,20,71,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,0,1,0,1,1,1,1,3,1,22,8,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,31,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,
        3,43,8,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,51,8,3,10,3,12,3,54,9,3,1,4,
        1,4,1,5,1,5,1,5,1,5,5,5,62,8,5,10,5,12,5,65,9,5,3,5,67,8,5,1,5,1,
        5,1,5,0,1,6,6,0,2,4,6,8,10,0,3,1,0,1,3,1,0,4,5,1,0,8,11,76,0,13,
        1,0,0,0,2,21,1,0,0,0,4,30,1,0,0,0,6,42,1,0,0,0,8,55,1,0,0,0,10,57,
        1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,
        15,16,1,0,0,0,16,17,1,0,0,0,17,18,5,0,0,1,18,1,1,0,0,0,19,22,3,4,
        2,0,20,22,3,6,3,0,21,19,1,0,0,0,21,20,1,0,0,0,22,3,1,0,0,0,23,24,
        5,16,0,0,24,25,5,15,0,0,25,31,3,6,3,0,26,27,5,16,0,0,27,28,3,8,4,
        0,28,29,3,6,3,0,29,31,1,0,0,0,30,23,1,0,0,0,30,26,1,0,0,0,31,5,1,
        0,0,0,32,33,6,3,-1,0,33,34,5,6,0,0,34,35,3,6,3,0,35,36,5,7,0,0,36,
        43,1,0,0,0,37,43,5,16,0,0,38,43,5,17,0,0,39,43,5,18,0,0,40,43,5,
        19,0,0,41,43,3,10,5,0,42,32,1,0,0,0,42,37,1,0,0,0,42,38,1,0,0,0,
        42,39,1,0,0,0,42,40,1,0,0,0,42,41,1,0,0,0,43,52,1,0,0,0,44,45,10,
        8,0,0,45,46,7,0,0,0,46,51,3,6,3,9,47,48,10,7,0,0,48,49,7,1,0,0,49,
        51,3,6,3,8,50,44,1,0,0,0,50,47,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,
        0,52,53,1,0,0,0,53,7,1,0,0,0,54,52,1,0,0,0,55,56,7,2,0,0,56,9,1,
        0,0,0,57,66,5,12,0,0,58,63,3,6,3,0,59,60,5,13,0,0,60,62,3,6,3,0,
        61,59,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,67,1,
        0,0,0,65,63,1,0,0,0,66,58,1,0,0,0,66,67,1,0,0,0,67,68,1,0,0,0,68,
        69,5,14,0,0,69,11,1,0,0,0,8,15,21,30,42,50,52,63,66
    ]

class PythonSubsetParser ( Parser ):

    grammarFileName = "PythonSubset.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'%'", "'+'", "'-'", "'('", 
                     "')'", "'+='", "'-='", "'*='", "'/='", "'['", "','", 
                     "']'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ASSIGN", "IDENTIFIER", 
                      "INT", "FLOAT", "STRING", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_expr = 3
    RULE_compoundAssign = 4
    RULE_array = 5

    ruleNames =  [ "program", "statement", "assignment", "expr", "compoundAssign", 
                   "array" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    ASSIGN=15
    IDENTIFIER=16
    INT=17
    FLOAT=18
    STRING=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PythonSubsetParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonSubsetParser.StatementContext)
            else:
                return self.getTypedRuleContext(PythonSubsetParser.StatementContext,i)


        def getRuleIndex(self):
            return PythonSubsetParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = PythonSubsetParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.statement()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 987200) != 0)):
                    break

            self.state = 17
            self.match(PythonSubsetParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(PythonSubsetParser.AssignmentContext,0)


        def expr(self):
            return self.getTypedRuleContext(PythonSubsetParser.ExprContext,0)


        def getRuleIndex(self):
            return PythonSubsetParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = PythonSubsetParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PythonSubsetParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(PythonSubsetParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(PythonSubsetParser.ExprContext,0)


        def compoundAssign(self):
            return self.getTypedRuleContext(PythonSubsetParser.CompoundAssignContext,0)


        def getRuleIndex(self):
            return PythonSubsetParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = PythonSubsetParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(PythonSubsetParser.IDENTIFIER)
                self.state = 24
                self.match(PythonSubsetParser.ASSIGN)
                self.state = 25
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(PythonSubsetParser.IDENTIFIER)
                self.state = 27
                self.compoundAssign()
                self.state = 28
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonSubsetParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonSubsetParser.ExprContext,i)


        def IDENTIFIER(self):
            return self.getToken(PythonSubsetParser.IDENTIFIER, 0)

        def INT(self):
            return self.getToken(PythonSubsetParser.INT, 0)

        def FLOAT(self):
            return self.getToken(PythonSubsetParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(PythonSubsetParser.STRING, 0)

        def array(self):
            return self.getTypedRuleContext(PythonSubsetParser.ArrayContext,0)


        def getRuleIndex(self):
            return PythonSubsetParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonSubsetParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 33
                self.match(PythonSubsetParser.T__5)
                self.state = 34
                self.expr(0)
                self.state = 35
                self.match(PythonSubsetParser.T__6)
                pass
            elif token in [16]:
                self.state = 37
                self.match(PythonSubsetParser.IDENTIFIER)
                pass
            elif token in [17]:
                self.state = 38
                self.match(PythonSubsetParser.INT)
                pass
            elif token in [18]:
                self.state = 39
                self.match(PythonSubsetParser.FLOAT)
                pass
            elif token in [19]:
                self.state = 40
                self.match(PythonSubsetParser.STRING)
                pass
            elif token in [12]:
                self.state = 41
                self.array()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 50
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = PythonSubsetParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 45
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 46
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = PythonSubsetParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 47
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 48
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 49
                        self.expr(8)
                        pass

             
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CompoundAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonSubsetParser.RULE_compoundAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundAssign" ):
                listener.enterCompoundAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundAssign" ):
                listener.exitCompoundAssign(self)




    def compoundAssign(self):

        localctx = PythonSubsetParser.CompoundAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_compoundAssign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonSubsetParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonSubsetParser.ExprContext,i)


        def getRuleIndex(self):
            return PythonSubsetParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = PythonSubsetParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(PythonSubsetParser.T__11)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 987200) != 0):
                self.state = 58
                self.expr(0)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 59
                    self.match(PythonSubsetParser.T__12)
                    self.state = 60
                    self.expr(0)
                    self.state = 65
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 68
            self.match(PythonSubsetParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         




